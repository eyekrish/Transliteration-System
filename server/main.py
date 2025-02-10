from fastapi import FastAPI
from pydantic import BaseModel
from CSM import mapping
from starlette.middleware.cors import CORSMiddleware
from tokenizer import tokenize_word_to_consonants_vowels

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransliterateReq(BaseModel):
    text: str

@app.post('/')
async def transliterate(text: TransliterateReq):
    words = text.text.split()
    transliterated_words = []
    all_independent_vowels = []
    all_consonants = []
    all_dependent_vowels = []
    all_digits = []
    all_spaces = []
    all_symbols = []
    all_punctuation = []

    for word in words:
        independent_vowels, consonants, dependent_vowels, digits, spaces, symbols, punctuation = tokenize_word_to_consonants_vowels(word)

        all_independent_vowels.extend(independent_vowels)
        all_consonants.extend(consonants)
        all_dependent_vowels.extend(dependent_vowels)
        all_digits.extend(digits)
        all_spaces.extend(spaces)
        all_symbols.extend(symbols)
        all_punctuation.extend(punctuation)

        transliterated_chars = []


        for i in range(len(word) - 1):
            cur = word[i]
            next = word[i+1]

            if cur in mapping:
                char_type = mapping[cur]["type"]
                next_char_type = mapping[next]["type"]

                # print(f"{cur}\n{char_type} {next}\n{ord(next)}")

                if (char_type == 'dependent_vowel') or (char_type == 'symbols'):
                    continue

                if((next_char_type == 'dependent_vowel') or (next_char_type == 'symbols') or (next_char_type == 'punctuation')) and ((char_type == 'consonant') or (char_type == 'vowel')):
                    joined = cur+next
                    if joined in mapping:
                        transliterated_chars.append(mapping[joined].get('char',""))

                elif(char_type=='consonant'):
                    transliterated_chars.append(mapping[cur]["char"])
                    transliterated_chars.append("a")

                else:
                    transliterated_chars.append(mapping[cur]["char"])

        if(mapping[word[-1]]['type']=="dependent_vowel") or (mapping[word[-1]]['type']=="symbols") or (mapping[word[-1]]['type']=="punctuation"):
            if(len(word==1)):
                transliterated_chars.append(mapping[word[-1]]['char'])
            else:
                pass
        else:
            transliterated_chars.append(mapping[word[-1]]['char'])


        transliterated_word = "".join(transliterated_chars)
        transliterated_words.append(transliterated_word)

    transliterated_text = " ".join(transliterated_words)

    return {
        'ans': transliterated_text,
        'independent_vowels': list(set(all_independent_vowels)),
        'consonants': list(set(all_consonants)),
        'dependent_vowels': list(set(all_dependent_vowels)),
        'digits': list(set(all_digits)),
        'spaces': list(set(all_spaces)),
        'symbols': list(set(all_symbols)),
        'punctuation': list(set(all_punctuation))
    }


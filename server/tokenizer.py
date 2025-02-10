from CSM import mapping

def tokenize_word_to_consonants_vowels(word):
    independent_vowel_characters = []
    consonant_characters = []
    dependent_vowels_characters = []
    digits = []
    spaces = []
    symbols= []
    punctuation= []
    
    for char in word:
        char_info = mapping.get(char)
        if char_info:
            char_type = char_info.get("type")
            if char_type == "vowel":
                independent_vowel_characters.append(char)
            elif char_type == "consonant":
                consonant_characters.append(char)
            elif char_type == "dependent_vowel":
                dependent_vowels_characters.append(char)
            elif char_type == "digits":
                digits.append(char)
            elif char_type == "space":
                spaces.append(char)
            elif char_type == "symbols":
                symbols.append(char)
            elif char_type == "punctuation":
                punctuation.append(char)
    return (
        independent_vowel_characters,
        consonant_characters,
        dependent_vowels_characters,
        digits,
        spaces,
        symbols,
        punctuation,
    )

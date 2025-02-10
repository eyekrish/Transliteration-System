import { useState } from 'react';
import './index.css';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [categories, setCategories] = useState({
    independent_vowels: [],
    consonants: [],
    dependent_vowels: [],
    digits: [],
    spaces: [],
    symbols: [],
    punctuation: []
  });

  const handleChange = (e) => {
    setInput(e.target.value);
  };

  const submitclick = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`http://127.0.0.1:8000/`, { 'text': input });
      setOutput(response.data.ans);
      setCategories({
        independent_vowels: response.data.independent_vowels,
        consonants: response.data.consonants,
        dependent_vowels: response.data.dependent_vowels,
        digits: response.data.digits,
        spaces: response.data.spaces,
        symbols: response.data.symbols,
        punctuation: response.data.punctuation
      });
    } catch (error) {
      console.error("Error occurred while transliterating:", error);
    }
  };

  return (
    <>  
      <div className='flex flex-col items-center justify-center min-h-screen w-screen p-4'>
        <div className='w-full max-w-lg md:max-w-xl lg:max-w-2xl'>
          <div className='text-2xl md:text-3xl font-bold mt-2 min-h-[500px] md:min-h-[600px] w-full bg-gray-200 text-center rounded-2xl p-4 md:p-8'>
            <div className='text-lg md:text-xl flex flex-col mt-4'>
              <p className='p-4 text-2xl md:text-3xl text-center'>Transliteration System For Pracalit Script</p>
              <div className='p-4 flex flex-col items-start'>
                <label htmlFor="Pracalit" className="block mb-2 text-md font-medium text-black">Text in Pracalit</label>
                <textarea 
                  name="Pracalit" 
                  onChange={handleChange} 
                  id="pracalit_text" 
                  className='text-md p-2 block w-full font-medium rounded-lg resize-y min-h-[200px] overflow-auto' 
                  placeholder='Namaste'
                />
              </div>
              <div className='p-4 flex flex-col items-start'>
                <label htmlFor="Transliterated Text" className="block mb-2 text-md font-medium text-black">Transliterated Text</label>
                <textarea 
                  value={output} 
                  id="transliterated_text" 
                  name="Transliterated Text" 
                  disabled 
                  className='bg-white text-md p-2 block w-full font-medium rounded-lg resize-y min-h-[200px] overflow-auto' 
                  placeholder='Result'
                />
              </div>
            </div>  
            <button 
              type="submit" 
              onClick={submitclick} 
              className='mt-3 bg-blue-700 text-white rounded-2xl p-2 w-full md:w-auto'
            >
              Submit
            </button>

            <div className='text-sm mt-7 text-gray-800'>
              <div className="category"><strong>Independent Vowels:</strong> {categories.independent_vowels.join(', ')}</div>
              <div className="category"><strong>Consonants:</strong> {categories.consonants.join(', ')}</div>
              <div className="category"><strong>Dependent Vowels:</strong> {categories.dependent_vowels.join(', ')}</div>
              <div className="category"><strong>Digits:</strong> {categories.digits.join(', ')}</div>
              <div className="category"><strong>Symbols:</strong> {categories.symbols.join(', ')}</div>
              <div className="category"><strong>Punctuation:</strong> {categories.punctuation.join(', ')}</div>
            </div>

          </div>
        </div>
      </div>
    </>
  );
}

export default App;

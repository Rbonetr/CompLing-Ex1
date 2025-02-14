## Importing libraries
import re # will be using this to clean the data
import operator 
from operator import itemgetter  # will be using this for clarity and to help sort the data
import string  # TODO 
import nltk 
nltk.download('punkt')  #Download NLTK data files (if not already downloaded)
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer  
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np

## Defining a function to analye the text data: tokenize, create dictionaries and plot.
def process_text(text, language):
    # Tokenizing the text into words
    pattern = r'[a-zA-Z]+(?:\.[a-zA-Z]+)*|\d+(?:,\d+)*(?:\.\d+)?'
    tokenizer = RegexpTokenizer(pattern)
    tokens = tokenizer.tokenize(text)
    
    # Creating a sorted dictionary of words and their frequencies
    word_frequency_dict = {}
    for word in tokens:
        if word in word_frequency_dict:
            word_frequency_dict[word] += 1
        else:
            word_frequency_dict[word] = 1

    sort_freq_dict = dict(sorted(word_frequency_dict.items(), key=itemgetter(1), reverse=True))
    
    # Creating a sorted dictionary of words by their lengths
    word_length_dict = {word: len(word) for word in tokens}
    sort_length_dict = dict(sorted(word_length_dict.items(), key=itemgetter(1), reverse=False))
    
    # Defining variables for the plot that will allow comparison of word lengths and their frequencies
    words = list(sort_length_dict.keys())
    lengths = list(sort_length_dict.values())
    frequencies = [word_frequency_dict[word] for word in sort_length_dict.keys()]
    
    # Creating plot
    plt.figure(figsize=(15, 6))
    plt.scatter(range(len(words)), frequencies, alpha=0.7)
    plt.yscale('log')
    plt.title(f'{language}: Word Length vs Frequency')
    plt.xlabel('Word Length: range from shortest to longest')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Calculating the average word length for the document
    average_length = sum(lengths) / len(lengths)
    print(f"Average word length in {language} document: {average_length:.2f}")
    
    return tokens, word_frequency_dict, word_length_dict, sort_length_dict, lengths, frequencies


#### ENGLISH DATA ####

## Opening the file and processing its content. Then, cleaning it.
with open("Adm_ENG.txt", "r", encoding="utf-8") as file:
    DocEng = file.read()
    DocEng = DocEng.lower()  # Lowercasing the text
    DocEng = DocEng.replace("\n", " ")  # Replacing new lines with spaces
    DocEng = re.sub(r'\([a-z]\)', '', DocEng)  # Removing brackets with single letters inside, used for enumerations
    DocEng = re.sub(r'[^\w\s]', '', DocEng)  # Removing punctuation
    DocEng = re.sub(r'\d+', '', DocEng)  # Removing numbers
    DocEng = re.sub(r'\s+', ' ', DocEng)  # Removing extra spaces
    DocEng = re.sub(r'\b(?:ii|iii|iv|v|vi|vii|viii|ix|x|xi)\b', '', DocEng)  # Removing Roman numerals

# Process the English text
tokens_eng, word_frequency_dict_eng, word_length_dict_eng, sort_length_dict_eng, lengths_eng, frequencies_eng = process_text(DocEng, "ENG")


#### CATALAN DATA ####

## Opening the file and processing its content. Then, cleaning it.
with open("Adm_CAT.txt", "r", encoding="utf-8") as file:
    DocCat = file.read()
    DocCat = DocCat.lower()  # Lowercasing the text
    DocCat = DocCat.replace("\n", " ")  # Replacing new lines with spaces
    DocCat = re.sub(r'\([a-z]\)', '', DocCat)  # Removing brackets with single letters inside, used for enumerations
    DocCat = re.sub(r'\d+', '', DocCat)  # Removing numbers
    DocCat = re.sub(r'\b(?:ii|iii|iv|v|vi|vii|viii|ix|x)\b', '', DocCat)  # Removing Roman numerals

# Handling Catalan contractions and character issues:
'''Apparently, in the process of tokenization with NLTK the vowels with an ortographic accent are not properly recognized.
They are converted into a blank space, causing words such as "justícia" to be split into "just" and "cia".
While not ideal, the best solution I could come up with was to remove the accents from the text.
The same happened with contractions (t', d', etc.), so I changed them to their full form.'''
# Replace "l'" followed by a word ending with "a" with "la". While not perfect, the vast majority of feminine words that may have "l'" in front of them end with "a", in catalan.
DocCat = re.sub(r"\bl'(\w*a\b)", r"la \1", DocCat)
# Other contractions and issues:
contractions = {
    r"\bl'": "el ",
    r"\bd'": "de ",
    r"\bm'": "me ",
    r"\bn'": "en ",
    r"\bs'": "se ",
    r"\bt'": "te ",
    r"\bdel\b": "de el ",
    r"\bdels\b": "de els ",
    r"\bpel\b": "per el ",
    r"\bpels\b": "per els ",
    r"\bal\b": "a el ",
    r"à": "a",
    r"é": "e",
    r"è": "e",
    r"í": "i",
    r"ò": "o",
    r"ó": "o",
    r"ú": "u",
    r"ü": "u",
    r"ï": "i",
    r"ç": "c",
}

for contraction, expanded in contractions.items():
    DocCat = re.sub(contraction, expanded, DocCat)

DocCat = re.sub(r'[^\w\s]', '', DocCat)  # Removing punctuation
DocCat = re.sub(r'\s+', ' ', DocCat)  # Removing extra spaces

# Process the Catalan text
tokens_cat, word_frequency_dict_cat, word_length_dict_cat, sort_length_dict_cat, lengths_cat, frequencies_cat = process_text(DocCat, "CAT")


### The two plots side by side ##
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].scatter(range(len(lengths_eng)), frequencies_eng, alpha=0.7)
axes[0].set_yscale('log')
axes[0].set_title('ENG: Word Length vs Frequency (range)')
axes[0].set_xlabel('Word Length')
axes[0].set_ylabel('Frequency')
axes[0].grid(True)

axes[1].scatter(range(len(lengths_cat)), frequencies_cat, alpha=0.7)
axes[1].set_yscale('log')
axes[1].set_title('CAT: Word Length vs Frequency (range)')
axes[1].set_xlabel('Word Length')
axes[1].set_ylabel('Frequency')
axes[1].grid(True)

plt.tight_layout()
plt.show()

### Plots with words with the same length stacked together for better clarity (SIMPLIFIED)
# English
plt.figure(figsize=(15, 6))
plt.scatter(lengths_eng, frequencies_eng, alpha=0.7)
plt.yscale('log')
plt.title('ENG: Word Length vs Frequency')
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(ticks=range(min(lengths_eng), max(lengths_eng) + 1))  # Set x-axis intervals to 1
plt.tight_layout()
plt.show()
# Catalan
plt.figure(figsize=(15, 6))
plt.scatter(lengths_cat, frequencies_cat, alpha=0.7)
plt.yscale('log')
plt.title('CAT: Word Length vs Frequency')
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(ticks=range(min(lengths_cat), max(lengths_cat) + 1))  # Set x-axis intervals to 1
plt.tight_layout()
plt.show()

#### ALTERNATIVE: REMOVING STOPWORDS ####
## English
stop_words = set(stopwords.words('english'))
filtered_words_eng = [word for word in tokens_eng if word not in stop_words]

# Process the filtered English text
_, filtered_word_frequency_dict_eng, filtered_word_length_dict_eng, filtered_sort_length_dict_eng, filtered_lengths_eng, filtered_frequencies_eng = process_text(' '.join(filtered_words_eng), "ENG (filtered)")

## Catalan
stop_words_cat = set(stopwords.words('catalan'))
filtered_words_cat = [word for word in tokens_cat if word not in stop_words_cat]

# Process the filtered Catalan text
_, filtered_word_frequency_dict_cat, filtered_word_length_dict_cat, filtered_sort_length_dict_cat, filtered_lengths_cat, filtered_frequencies_cat = process_text(' '.join(filtered_words_cat), "CAT (filtered)")

## SIMPLIFIED PLOTS
# English
plt.figure(figsize=(15, 6))
plt.scatter(filtered_lengths_eng, filtered_frequencies_eng, alpha=0.7)
plt.yscale('log')
plt.title('ENG: Word Length vs Frequency (filtered)')
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(ticks=range(min(filtered_lengths_eng), max(filtered_lengths_eng) + 1))  # Set x-axis intervals to 1
plt.tight_layout()
plt.show()
# Catalan
plt.figure(figsize=(15, 6))
plt.scatter(filtered_lengths_cat, filtered_frequencies_cat, alpha=0.7)
plt.yscale('log')
plt.title('CAT: Word Length vs Frequency (filtered)')
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(ticks=range(min(filtered_lengths_cat), max(filtered_lengths_cat) + 1))  # Set x-axis intervals to 1
plt.tight_layout()
plt.show()

##END##
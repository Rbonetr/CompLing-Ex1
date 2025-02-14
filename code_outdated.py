## Importing libraries
import re
import operator #will be using this to help sort the data
from operator import itemgetter #will be using this for clarity and to help sort the data
import string #TODO may use it to match smth?
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer #Just incase, probably will use SpaCy.
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np


#### ENGLISH DATA ####

## Opening the file and processing its content. Then, cleaning it.
with open("Adm_ENG.txt", "r", encoding="utf-8") as file:
    DocEng = file.read()
    DocEng = DocEng.lower() #Lowercasing the text
    DocEng = DocEng.replace("\n", " ") #Replacing new lines with spaces
    DocEng = re.sub(r'\([a-z]\)', '', DocEng) #Removing brackets with single letters inside, used for ennumerations
    DocEng = re.sub(r'[^\w\s]', '', DocEng) #Removing punctuation
    DocEng = re.sub(r'\d+', '', DocEng) #Removing numbers
    DocEng = re.sub(r'\s+', ' ', DocEng) #Removing extra spaces
    DocEng = re.sub(r'\b(?:ii|iii|iv|v|vi|vii|viii|ix|x|xi)\b', '', DocEng) #Removing roman numerals

## Tokenizing the text into words
pattern = r'[a-zA-Z]+(?:\.[a-zA-Z]+)*|\d+(?:,\d+)*(?:\.\d+)?'
tokenizer = RegexpTokenizer(pattern)
tokens = tokenizer.tokenize(DocEng)
'''TEST print(tokens[:1000])'''

## Creating a sorted dictionary of the words by their frequencies
word_frequency_dict = {}
for word in tokens:
    if word in word_frequency_dict:
        word_frequency_dict[word] += 1
    else:
        word_frequency_dict[word] = 1

sort_freq_dict = dict(sorted(word_frequency_dict.items(), key=itemgetter(1), reverse=True))
'''TEST print (sort_freq_dict)''' #sorted frequency dictionary

## Creating a sorted dictionary of words by their lengths
word_length_dict = {word: len(word) for word in tokens}
sort_length_dict = dict(sorted(word_length_dict.items(), key=itemgetter(1), reverse=False))
'''TEST print(sort_length_dict)''' #sorted length dictionary (shortest to longest)

## Defining variables for the plot that will allow comparison of word length and their frequencies
words = list (sort_length_dict.keys())
lengths = list(sort_length_dict.values())
frequencies = [word_frequency_dict[word] for word in sort_length_dict.keys()]

## Creating plot
plt.figure(figsize=(15, 6))
plt.scatter(range(len(words)), frequencies, alpha=0.7)
plt.yscale('log')
plt.title('ENG: Word Length vs Frequency')
plt.xlabel('Word Length: range from shortest to longest')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

## Calculating the average word length for the English document
average_length_eng = sum(lengths) / len(lengths)
print(f"Average word length in English document: {average_length_eng:.2f}")


#### CATALAN DATA ####

## Opening the file and processing its content. Then, cleaning it.
with open("Adm_CAT.txt", "r", encoding="utf-8") as file:
    DocCat = file.read()
    DocCat = DocCat.lower() #Lowercasing the text
    DocCat = DocCat.replace("\n", " ") #Replacing new lines with spaces
    DocCat = re.sub(r'\([a-z]\)', '', DocCat) #Removing brackets with single letters inside, used for ennumerations
    DocCat = re.sub(r'\d+', '', DocCat) #Removing numbers
    DocEng = re.sub(r'\b(?:ii|iii|iv|v|vi|vii|viii|ix|x|xi)\b', '', DocEng) #Removing roman numerals

#Handling Catalan contractions:
#Replace "l'" followed by a word ending with "a" with "la". While not perfect, the bast majority of feminine words that may have "l'" in front of them end with "a".
DocCat = re.sub(r"\bl'(\w*a\b)", r"la \1", DocCat)
#Other contractions:
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
}

for contraction, expanded in contractions.items():
    DocCat = re.sub(contraction, expanded, DocCat)

DocCat = re.sub(r'[^\w\s]', '', DocCat) #Removing punctuation
DocCat = re.sub(r'\s+', ' ', DocCat) #Removing extra spaces

## Tokenizing the text into words
Cpattern = r'[a-zA-Z]+(?:\.[a-zA-Z]+)*|\d+(?:,\d+)*(?:\.\d+)?'
Ctokenizer = RegexpTokenizer(Cpattern)
Ctokens = Ctokenizer.tokenize(DocCat)
'''TEST print(tokens[:1000])'''

#Creating a sorted dictionary of words and their frequencies
Cword_frequency_dict = {}
for word in Ctokens:
    if word in Cword_frequency_dict:
        Cword_frequency_dict[word] += 1
    else:
        Cword_frequency_dict[word] = 1

Csort_freq_dict = dict(sorted(Cword_frequency_dict.items(), key=itemgetter(1), reverse=True))
'''TEST print(sort_freq_dict) #sorted frequency dictionary'''

## Creating a sorted dictionary of words by their lengths
Cword_length_dict = {word: len(word) for word in Ctokens}
Csort_length_dict = dict(sorted(Cword_length_dict.items(), key=itemgetter(1), reverse=False))
'''TEST print(sort_length_dict) #sorted length dictionary'''

## Defining variables for the plot that will allow comparison of word lengths and their frequencies
Cwords = list (Csort_length_dict.keys())
Clengths = list(Csort_length_dict.values())
Cfrequencies = [Cword_frequency_dict[word] for word in Csort_length_dict.keys()]

## Creating plot ()
plt.figure(figsize=(15, 6))
plt.scatter(range(len(Cwords)), Cfrequencies, alpha=0.7)
plt.yscale('log')
plt.title('CAT: Word Length vs Frequency')
plt.xlabel('Word Length: range from shortest to longest')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout() #Adjusting the layout to fit the labels
plt.show()

## Calculating the average word length for the Catalan document
average_length_cat = sum(Clengths) / len(Clengths)
print(f"Average word length in Catalan document: {average_length_cat:.2f}")

### The two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].scatter(range(len(words)), frequencies, alpha=0.7)
axes[0].set_yscale('log')
axes[0].set_title('ENG: Word Length vs Frequency (range)')
axes[0].set_xlabel('Word Length')
axes[0].set_ylabel('Frequency')
axes[0].grid(True)

axes[1].scatter(range(len(Cwords)), Cfrequencies, alpha=0.7)
axes[1].set_yscale('log')
axes[1].set_title('CAT: Word Length vs Frequency (range)')
axes[1].set_xlabel('Word Length')
axes[1].set_ylabel('Frequency')
axes[1].grid(True)

plt.tight_layout()
plt.show()


### Plots with words with the same lenght stacked together for better clarity (simplified)
# English
plt.figure(figsize=(15, 6))
plt.scatter(lengths, frequencies, alpha=0.7)
plt.yscale('log')
plt.title('ENG: Word Length vs Frequency')
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(ticks=range(min(lengths), max(lengths) + 1)) # Set x-axis intervals to 1
plt.tight_layout()
plt.show()
# Catalan
plt.figure(figsize=(15, 6))
plt.scatter(Clengths, Cfrequencies, alpha=0.7)
plt.yscale('log')
plt.title('CAT: Word Length vs Frequency')
plt.xlabel('Word Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(ticks=range(min(Clengths), max(Clengths) + 1)) # Set x-axis intervals to 1
plt.tight_layout()
plt.show()


#### ALTERNATIVE: REMOVING STOPWORDS ####
# English
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word not in stop_words]
filtered_word_frequency_dict = {}
for word in filtered_words:
    if word in filtered_word_frequency_dict:
        filtered_word_frequency_dict[word] += 1
    else:
        filtered_word_frequency_dict[word] = 1

'''Switched part of the code to a defined process to aviod unnecessary repetition. Check code_ex1.py for the continuation. :) '''

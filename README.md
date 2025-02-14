EXERCISE 1: Zipf's Law OF ABBREVIATION	                        

**INTRODUCTION**

**> What is Zipf's Law of abbreviation?**

It’s a linguistic principle which claims that the more frequent a word is, the shorter it tends to be. This occurs with the aim of maximizing efficiency while improving clarity. Some studies show that the principle holds not only for length in letters but also for acoustic duration.

**> What languages will be examined?**

Two sets of data will be analyzed to observe and test this principle. English will be the first, and I have chosen Catalan for the second. I selected it because it’s my mother tongue, and I already know it well, as I studied a Catalan philology degree.

It may also be good for this exercise to compare a synthetic language (English) —which creates words by combining, such as “wheelchair”— and an analytic language (Catalan) —which, instead, creates phrases such as “cadira de rodes”. Even though Catalan has a richer inflectional morphology, this is not as significant, so English should have longer words than Catalan on average. This comparison is particularly interesting when analyzing Zipf's Law of abbreviation, because English is a language that is used much more than Catalan on a daily basis.

**> What genre will you test and why?**

Administrative documents. I think it’s interesting to see if Zipf's Law of abbreviation holds in contexts where the speakers pay attention to their language and try to be formal. We will see how well this law applies in a context that is often described as wordy.

**> Expectations:**

My expectations are that there will be a tendency for the most used words to be short. I also think that, because of the administrative language, some longer words will appear more often.
Overall, I expect English words to be shorter on average than Catalan words. This is counterintuitive given that English is a synthetic language and Catalan is an analytic one. However, this may hold because of English being more used and having more second-language learners.

**MATERIAL**

I opted to take documents from the European Union that are available in both English and Catalan. This way, the content of the texts will be very similar, which will help eliminate potential data biases. The data was gathered from EUR-Lex and Portal jurídic de Catalunya.

- Consolidated version of the Treaty establishing the European Atomic Energy Community (2016) – Without annexes.
- Consolidated version of the Treaty on European Union (2012, ENG – 2016, CAT)

I copied the texts in a .txt document, one for English (Adm_ENG) and one for Catalan (Adm_CAT). At first, I was planning to use SpaCy. However, I had issues downloading en_core_web_sm to my computer (I worked with Visual Studio in Anaconda). After investigating, I think the problem may be due to an incompatibility of some necessary libraries for SpaCy (wheel, thinc) and the newest python versions (I worked with 3.12.4). Since I was not succeeding in solving the issue, I decided to work with NLTK libraries.

**METHODS**

When cleaning the data for tokenization, some issues appeared. I eliminated unwanted characters for enumeration (eg. (a), (b), (IV), (VIII)), but couldn’t work around the roman numeral I (one), so it was left.
NLTK tokenization doesn’t properly recognize accented vowels in Catalan (à, é, etc.). It replaces them with a blank space, which leads to a false splitting of words. Moreover, the removal of punctuation marks erases apostrophes, which causes significant errors in Catalan, as then all articles unite with the following word. To solve these issues, a part of code was made to substitute all accented vowels for their non-accented counterparts and the contractions for their full form.

For more comparison, I analyzed the data both with and without stopwords. In the version without stopwords, it would have been great to lemmatize the words, but in my judgement, NLTK doesn’t do a proper job on that, and the results may not be accurate. Because of having to repeat the process of tokenization and creation of dictionaries for four datasets, I eventually restructured the initial content (code_outdated.py) in a new code (code_ex1.py) where I defined a function that can run for the different data.

**RESULTS**

The law holds in a similar way for both English and Catalan in administrative language. In Fig. 1 and Fig. 2 we can appreciate higher frequencies on shorter words. These results are clearer in Fig. 3 and Fig. 4, because we can see that there are fewer words containing 1, 2, or even 3 letters, thus meaning a higher percentage of these words being highly frequent.
However, these results may not follow the principle as well as language outside the administration. The cause may be a tendency of administrative language being more artificial and wordy. This is suggested by the high average of word length in this study’s data: 7.85 in English and 8.35 in Catalan (without stopwords, 7.97 and 8.44 respectively). It could be interesting to do a more extensive comparison on this genre’s word length.

The length averages confirm one hypothesis: Catalan words are longer on average even though its structure should intuitively mean being shorter than English words. This opens the question of whether, and to which extent, this is due to English being more learned as a second language and used overall. If affirmative, Zipf's Law of abbreviation can be seen not only in one language’s words, but also between languages.
On the data without stopwords (Fig. 5-Fig. 8) we can see a more attenuated effect. While some light correlation may be there, more data and a study of significance should be done to determine to which extent we can say this law applies to administrative language if stopwords are removed.

With this analysis it has been able to study the phenomenon and to answer to expectations. However, its results should be treated with caution as the data is too small to generalize and it’s not cleaned perfectly, with NLTK. Ideally, this should be done with a better library, SpaCy, and a lot more data.

*_The Figures are the plots generated by the code, in order_

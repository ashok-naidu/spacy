#Stop words
#importing stop words from English language.
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

print('spaCy Version: %s' % (spacy.__version__))

nlp = spacy.load('en_core_web_sm')

spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS

#Printing the total number of stop words:
print('Number of stop words: %d' % len(spacy_stopwords))

#Printing first ten stop words:
print('First ten stop words: %s' % list(spacy_stopwords)[:20])


text='Instead, we’ll create an empty list called filtered_sent and then iterate through our doc variable to look at each tokenized word from our source text. spaCy includes a bunch of helpful token attributes, and we’ll use one of them called is_stop to identify words that aren’t in the stopword list and then append them to our filtered_sent list.'

#Implementation of stop words:
filtered_sent=[]

#  "nlp" Object is used to create documents with linguistic annotations.
doc = nlp(text)

# filtering stop words
for word in doc:
    if word.is_stop==False:
        filtered_sent.append(word)
print("Filtered Sentence:",filtered_sent)
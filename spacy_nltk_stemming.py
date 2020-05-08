import nltk
import spacy

from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

stemmer = PorterStemmer()
stemmersnowball = SnowballStemmer(language='english')

sp = spacy.load('en_core_web_sm')

tokens = ['compute', 'computer', 'computed', 'computing']


for token in tokens:
    print(token + ' --> ' + stemmer.stem(token))
    
    
    
for token in tokens:
    print(token + ' --> ' + stemmersnowball.stem(token))
    
sentence6 = sp(u'compute computer computed computing')

for word in sentence6:
    print(word.text,  word.lemma_)
    
sentence7 = sp(u'A letter has been written, asking him to be released')

for word in sentence7:
    print(word.text + '  ===>', word.lemma_)    
    
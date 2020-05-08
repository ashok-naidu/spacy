import spacy
nlp = spacy.load('en_core_web_sm')

# Import spaCy Matcher
from spacy.matcher import Matcher


doc1 = nlp("You read this book")
doc2 = nlp("I will book my ticket")

for token in doc1:
    # Print the token and its part-of-speech tag
    print(token.text, "-->", token.pos_ , "-->",  token.dep_)
    
    

for token in doc2:
    # Print the token and its part-of-speech tag
    print(token.text, "-->", token.pos_ , "-->",  token.dep_)


#Lets start using matchers

pattern = [{'TEXT': 'book', 'POS': 'VERB'}]

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)
matcher.add('rule_2', None, pattern)

matches = matcher(doc1)

print(matches)


matches = matcher(doc2)

print(matches)
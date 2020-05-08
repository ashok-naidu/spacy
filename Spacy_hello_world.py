import spacy
nlp = spacy.load('en_core_web_sm')

# Create an nlp object
doc = nlp("He went to play basketball")

#print(nlp.pipe_names)


# Iterate over the tokens
for token in doc:
    # Print the token and its part-of-speech tag
    print(token.text, "-->", token.pos_)

#print(spacy.explain("hi"))
    

# dependency parsing
for token in doc:
    print(token.text, "-->", token.dep_)    

print(spacy.explain("nsubj"), spacy.explain("ROOT"), spacy.explain("aux"), spacy.explain("advcl"), spacy.explain("dobj"))

#Named Entity Recognition using spaCy


doc = nlp("Indians spent over $71 billion on clothes in 2018")
 
for ent in doc.ents:
    print(ent.text, ent.label_)

doc = nlp("from 2002 Lex lives in united states")
 
for ent in doc.ents:
    print(ent.text, ent.label_)
print(spacy.explain("GPE"))
    

    
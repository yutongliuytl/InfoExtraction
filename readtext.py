import nltk
import string
from nltk.corpus import stopwords
import  spacy

nltk.download('stopwords')

def text_process(text):

    nopunc = [char for char in text]
    nopunc = ''.join(nopunc)
    print(nopunc)
    print('1')

    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


doc = open("hi.txt", 'r')
content = ' '.join(doc.readlines())

print(text_process(content))

nlp = spacy.load('en_core_web_sm')

doc = nlp(content)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

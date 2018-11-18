import nltk
import string
from nltk.corpus import stopwords
import  spacy


def text_process(text):

    nopunc = [char for char in text]
    nopunc = ''.join(nopunc)
    print(nopunc)
    print('1')

    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

def field_search(field_keys, ent, content): 

    start = ent.start_char
    if(start - 50 < 0):
        start = 50
    for word in field_keys:
        if(word.lower() in content[start-50:start].lower()):
            return ent.text
    

def NLP():

    doc = open("data.txt", 'r')
    content = ''.join(doc.readlines())

    birthday_keys = ["born", "birth"]
    origin_keys = ["from", "born", "birth", "my"]
    language_keys = ["speak", "first", "mother tongue", "native", "language"]
    person_keys = ["am", "name", "I am", "called", "I'm"]
    nationality_keys = ["am", "citizen", "is"]
    weight_keys = ["kg", "kilo", "weigh", "pounds", "lbs", "g"]
    height_keys = ["meter", "feet", "foot", "ft", "cm", "m"]
    income_keys = ["income", "salary", "pay", "receive", "make", "earn"]

    birthday = ''
    origin = ''
    language = ''
    person_first = ''
    person_last = ''
    nationality = ''
    weight = ''
    height = ''
    income = ''

    nlp = spacy.load('en_core_web_sm')

    doc = nlp(content)

    for ent in doc.ents:

        # Date of Birth
        if(ent.label_ == "DATE"):
            temp = field_search(birthday_keys, ent, content)
            if(temp is not None):
                birthday += " " + temp

        # Country
        if(ent.label_ == "GPE"):
            temp = field_search(origin_keys, ent, content)
            if(temp is not None):
                origin += " " + temp
                
        # Language
        if(ent.label_ == "LANGUAGE"):
            temp = field_search(language_keys, ent, content)
            if(temp is not None):
                language += " " + temp

        #first name
        #last name
        if(ent.label_ == "PERSON"):
            temp = field_search(person_keys, ent, content)
            if(temp is not None):
                person = temp
                first_last = person.split(" ")
                if(len(first_last) == 0):
                    person_first = first_last[0]
                if(len(first_last) > 1):
                    person_first = first_last[0]
                    person_last = first_last[-1]
                    
        #nationality
        if(ent.label_ == "NORP"):
            temp = field_search(nationality_keys, ent, content)
            if(temp is not None):
                nationality = temp

        #weight
        #height
        if(ent.label_ == "QUANTITY"):
            for key in weight_keys:
                if(key in ent.text):
                    weight = ent.text
            for key in height_keys:
                if(key in ent.text):
                    height = ent.text
        
        #income
        if(ent.label_ == "MONEY"):
            temp = field_search(income_keys, ent, content)
            if(temp is not None):
                income += " " + temp

    return birthday, origin, language, person_first, person_last, nationality, weight, height, income  
    


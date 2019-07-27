from string import punctuation
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS

from nltk.corpus import stopwords

stopwords = set(stopwords.words('french') + list(punctuation))

nlp = spacy.load("fr_core_news_md")

# stopwords = list(STOP_WORDS) + list(punctuation)

def tokenize(text):
    doc = nlp(text)
    liste = []
    for item in doc:
        liste.append(item.lemma_)
    liste = [mot for mot in liste if mot not in stopwords]
    liste = " ".join(liste)
    return nlp(liste)

def appartenir(topics, message):
    msg = tokenize(message)
    score = []
    for topic in topics:
        topic = tokenize(topic)
        score.append(msg.similarity(topic))
        print("message = ", message)
        print("topic = ", topic)
        print("score = ", msg.similarity(topic))
        print('-----------------------------------------------------------------------------')
    i = score.index(max(score))

    return topics[i]


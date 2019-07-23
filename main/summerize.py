from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import nltk
import string
from collections import defaultdict

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.wordnet import WordNetLemmatizer

from heapq import nlargest
import operator

stopwords = set(stopwords.words('french') + list(punctuation))


def summerize(text):
    sumlist = []
    sentences = sent_tokenize(text)

    def tokenize(text):
        tokens = nltk.word_tokenize(text)
        stems = []
        for item in tokens:
            stems.append(WordNetLemmatizer().lemmatize(item))
        return stems

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words=stopwords)
    tfs = tfidf.fit_transform([text])

    freqs = {}
    feature_names = tfidf.get_feature_names()
    for col in tfs.nonzero()[1]:
        freqs[feature_names[col]] = tfs[0, col]

    important_sentences = defaultdict(int)

    for i, sentence in enumerate(sentences):
        for token in word_tokenize(sentence.lower()):
            if token in freqs:
                important_sentences[i] += freqs[token]

    # Choose 20% of the text to show
    number_sentences = int(len(sentences) * 0.5)

    # Create an index with the most important sentences
    index_important_sentences = nlargest(number_sentences,
                                         important_sentences,
                                         important_sentences.get)

    # Sort frequencies
    sorted_freqs = sorted(
        freqs.items(), key=operator.itemgetter(1), reverse=True)

    # Create summary
    for i in sorted(index_important_sentences):
        sumlist.append(sentences[i])
    return "".join(sumlist)
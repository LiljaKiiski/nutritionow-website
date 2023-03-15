import nltk
from nltk.stem.lancaster import LancasterStemmer

import numpy
import tflearn
import tensorflow
import random
import sys

import json

stemmer = LancasterStemmer()

with open('FoodQandA.json') as file:
    data = json.load(file)


words = []
labels = []
docs_x = []
docs_y = []

for row in data:
    #print(data[row]["Question"])
    wrds = nltk.word_tokenize(data[row]["Question"])
    #words.extend(wrds)
    #docs_x.append(wrds)
    #docs_y.append(data[row]["Num"])

sys.exit()

for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
        
    if intent['tag'] not in labels:
        labels.append(intent['tag'])
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

#Extracting data

words = []
labels = []
docs_x = []
docs_y = []

for row in data:
    wrds = nltk.word_tokenize(data[row]["Question"])
    words.extend(wrds)
    docs_x.append(wrds)
    docs_y.append(data[row]["Num"])

    if data[row]["Num"] not in labels:
        labels.append(data[row]["Num"])

#Word stemming

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

#Bag of words

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

#Developing a Model

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

#Training and saving model

model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")
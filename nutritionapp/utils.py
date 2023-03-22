import torch.nn as nn
import random
import torch
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
import numpy as np
import random
import json

with open("staticfiles/json/intents.json", 'r') as f:
  intents = json.load(f)

stemmer = PorterStemmer()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out

def tokenize(sentence):
  return nltk.word_tokenize(sentence)

def stem(word):
  return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag
    
model_path = "staticfiles/models/data3.pth"
data = torch.load(model_path)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
    
bot_name = "Bobby"

def chat(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    # print(prob.item())
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return f"{bot_name}: {random.choice(intent['responses'])[0]}"
    else:
        return f"{bot_name}: I do not understand..."
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
# import keras.utils
import numpy as np
import tensorflow as tf
import sys

import pickle

tokenizer = pickle.load(open("tokenizer.pkl", 'rb'))
maxLen = pickle.load(open("maxLen.pkl", 'rb'))


try:
	model_dir = sys.argv[1]
except:
	model_dir = "./modeltf"

# # ---Load pickle Model---
# filename = "model.pkl"
# import pickle
# mdl = pickle.load(open(filename, 'rb'))

# --- Load tf model ---
localhost_save_option = tf.saved_model.SaveOptions(experimental_io_device="/job:localhost")
mdl = tf.keras.models.load_model(model_dir)

def makePrediction(inp, howMany):
	for i in range(howMany):
		token_list = tokenizer.texts_to_sequences([inp])[0]
		token_list = pad_sequences([token_list], maxlen=maxLen-1, padding='pre')
		predicted = np.argmax(mdl.predict(token_list, verbose=0), axis = -1)
		# predicted = mdl.predict(token_list, verbose=0)
		# print(predicted[0].shape)
		for word, index in tokenizer.word_index.items():
			# print(word, index)
			if index == predicted:
				inp = inp + " " + word
				break
	return inp

predictions = {}

def getProbabilityOf(context, input):
  try:
    predicted = predictions[context]
  except:
    token_list = tokenizer.texts_to_sequences([context])[0]
    token_list = pad_sequences([token_list], maxlen=maxLen-1, padding='pre')
    predicted = mdl.predict(token_list, verbose=0)
  try:
    res = predicted[0][tokenizer.word_index[input]]
  except:
    res = 1/10000
  return res


def calculateProb(sentence):
  sentence = sentence.lower()
  sentence = sentence.split()
  context = ""
  prob = 1
  for i in range(len(sentence)):
    prob *= getProbabilityOf(context, sentence[i])
    context += sentence[i]
  return prob


inputSentence = input("input sentence: ")
print(calculateProb(inputSentence))
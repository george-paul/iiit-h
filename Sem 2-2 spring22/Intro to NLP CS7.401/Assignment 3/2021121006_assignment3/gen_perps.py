from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import sys

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
import tensorflow as tf
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

# -------------------------------->
# print(makePrediction("bani is", 20))

predictions = {}
def loadPredictionsDict():
  print("<empty>")
  token_list = tokenizer.texts_to_sequences([""])[0]
  token_list = pad_sequences([token_list], maxlen=maxLen-1, padding='pre')
  predicted = mdl.predict(token_list, verbose=0)
  predictions[""] = predicted
  commonWords = list(tokenizer.word_index.keys())[:100]
  for i in commonWords:
    print(i)
    token_list = tokenizer.texts_to_sequences([i])[0]
    token_list = pad_sequences([token_list], maxlen=maxLen-1, padding='pre')
    predicted = mdl.predict(token_list, verbose=0)
    predictions[i] = predicted
loadPredictionsDict()
print(predictions)

sentences = []
with open("./europarl-corpus/test.europarl") as fr:
  sentences = fr.read().split("\n")

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
  
# print(getProbabilityOf("may there", "be", maxLen))

def calculatePerplexity(sentence):
  sentence = sentence.lower()
  sentence = sentence.split()
  context = ""
  prob = 1
  for i in range(len(sentence)):
    prob *= getProbabilityOf(context, sentence[i])
    context += sentence[i]
  return (1/prob)**(1/len(sentences))

# calculatePerplexity("We also need a framework directive, because the employees who are affected have been working in a grey zone for a long time now.")

perps = []
for i in range(len(sentences)):
  print(i)
  perps.append(calculatePerplexity(sentences[i]))

with open("./2021121006_LM_train.txt", "w") as fw:
  # average perplexity
  SUM = 0
  for i in perps:
    if i == np.inf:
      continue
    SUM += i
  print(SUM, len(perps))
  print(SUM/len(perps))
  fw.write(str(SUM/len(perps)) + "\n")
  for i in range(len(sentences)):
    fw.write(sentences[i] + "\t" + str(perps[i]) + "\n")
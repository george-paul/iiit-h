import numpy as np

data = ''
with open('./europarl-corpus/train.europarl') as f:
	noOfSentences = 10000
	for i in range(noOfSentences):
		data += f.readline()
# print(data)




from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import keras.utils

tokenizer = Tokenizer()

def dataset_preparation(data):
	sentences = data.lower().split('\n')
	tokenizer.fit_on_texts(sentences)
	vocabSize = len(tokenizer.word_index) + 1

	# print(vocabSize)

	tokenizedSentences = []
	for line in sentences:
		tokens = tokenizer.texts_to_sequences([line])[0]
		for i in range(1, len(tokens)):
			ngrams = tokens[:i+1]
			tokenizedSentences.append(ngrams)

	lens = [len(x) for x in tokenizedSentences]
	maxLen = max(lens)
	tokenizedSentences = np.array(pad_sequences(tokenizedSentences, maxlen=maxLen, padding='pre', dtype='uint8'))
	# print(tokenizedSentences.dtype)

	inputs, outputs = tokenizedSentences[:,:-1],tokenizedSentences[:,-1]
	outputs = keras.utils.np_utils.to_categorical(outputs, num_classes=vocabSize, dtype='uint8')
	# print(outputs.shape)

	return inputs, outputs, maxLen, vocabSize

# -------------------------------->
inputs, outputs, maxLen, vocabSize = dataset_preparation(data)


# save tokenizer and maxLen
import pickle
pickle.dump(tokenizer, open("tokenizer.pkl", 'wb'))
pickle.dump(maxLen, open("maxLen.pkl", 'wb'))


from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.callbacks import EarlyStopping
from keras.models import Sequential


def create_mdl(inputs, outputs, maxLen, vocabSize):
	
	mdl = Sequential()
	mdl.add(Embedding(vocabSize, 10, input_length=maxLen-1))
	mdl.add(LSTM(150, return_sequences = True))
	# mdl.add(Dropout(0.2))
	mdl.add(LSTM(100))
	mdl.add(Dense(vocabSize, activation='softmax'))

	# print("hi")

	mdl.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	earlystop = EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto')
	mdl.fit(inputs, outputs, epochs=1, verbose=1, callbacks=[earlystop])
	print(mdl.summary())
	return mdl

# -------------------------------->
mdl = create_mdl(inputs, outputs, maxLen, vocabSize)



# # ---Save Model---
# filename = 'winmodel.pkl'
# pickle.dump(mdl, open(filename, 'wb'))

model_dir = "./modeltf"

import tensorflow as tf
localhost_save_option = tf.saved_model.SaveOptions(experimental_io_device="/job:localhost")
mdl.save(model_dir + "tf.pkl", options=localhost_save_option)

#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import nltk
nltk.download('punkt')
import pandas as pd
import json


# In[4]:


jstring=[]
f = open('Electronics_5.json','r')
s = f.readline()

sentenceCount = 6000

for i in range(0, sentenceCount):
  jstring.append(json.loads(s)["reviewText"])
  s = f.readline()

len(jstring)


# In[5]:


text = jstring
text


# In[6]:


sentences = []
for i in text:
	sentences.append(nltk.tokenize.sent_tokenize(i))
# len(sentences)
sentences
# sentenceList = []
# for i in text:
# 	for j in i:
# 		sentenceCount


# In[7]:


sansPuncText = []
punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~+='''
# punctuations = "."
# print(punc)
for para in sentences:
	for sentence in para:
		newSent = sentence
		for punc in punctuations:
			newSent = newSent.replace(punc, "")
		sansPuncText.append(newSent)
sentences = sansPuncText


# In[8]:


# print(sentences)
tokens = []
for i in sentences:
	# for j in i:
		tokens.append(nltk.tokenize.word_tokenize(i))
tokens
# toks = []
# for i in tokens:
# 	for j in i:
# 		toks.append(j.upper())
# len(toks)
# toks


# In[9]:


vocab = {}
wordlist = []
for i in range(len(tokens)):
	for j in range(len(tokens[i])):
		tokens[i][j] = tokens[i][j].upper()
		if tokens[i][j] not in vocab.keys():
			vocab[tokens[i][j]] = len(wordlist)
			wordlist.append(tokens[i][j])
# tokens
# vocab
len(wordlist)


# In[10]:


len(vocab)
# np.iinfo('uint16').max


# In[11]:


windowSize = 3

coOccMatrix = np.zeros((len(vocab), len(vocab)), np.uint16)
for sentence in tokens:
	for i in range(len(sentence)):
		for j in range(windowSize):
			if i-1-j > 0:
				coOccMatrix[vocab[sentence[i]]][vocab[sentence[(i-1-j)]]] += 1
			if i+1+j < len(sentence):
				coOccMatrix[vocab[sentence[i]]][vocab[sentence[(i+1+j)]]] += 1

print(coOccMatrix)
print(coOccMatrix.shape)


# In[12]:


df=pd.DataFrame(coOccMatrix,index=vocab,columns=vocab)
df


# In[13]:


from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components=4)
# redCoc = np.zeros((len(vocab), len(vocab)), np.uint16)
redCoc = svd.fit_transform(df.values)
redCoc


# In[14]:


redCoc.shape


# In[15]:


from sklearn.manifold import TSNE
Y = TSNE().fit_transform(redCoc)


# In[16]:


# Y[0]
print(Y[:,0],Y[:,1])


# In[17]:


def distanceBetween(w1, w2):
	return abs((Y[vocab[w1]][0] - Y[vocab[w2]][0])**2 + (Y[vocab[w1]][1] - Y[vocab[w2]][1])**2)

def closestNWords(N, word):
	distances = []
	for i in range(len(wordlist)):
		distances.append((distanceBetween(wordlist[i], word), wordlist[i]))
	distances.sort()
	return distances[0:N]
		


# In[18]:


analysisWords = ["WE", "GPS", "GOT", "IS", "DECENT", "CAMERA"]
# analysisWords = ["WE", "GOT"]


# In[22]:


for word in analysisWords:
	print(word)
	for dw in closestNWords(11, word):
		print(dw[0], end = ' - ')
		print(dw[1])


# In[21]:



import matplotlib.pyplot as plot
for word in analysisWords:
	for dw in closestNWords(11, word):
		i = vocab[dw[1]]
		x = Y[i][0]
		y = Y[i][1]
		if(dw[0] == 0):
			plot.scatter(x,y, marker='x', color='red')
		else:
			plot.scatter(x,y, marker='x', color='blue')
		plot.text(x, y, dw[1], fontsize=8)
	plot.show()


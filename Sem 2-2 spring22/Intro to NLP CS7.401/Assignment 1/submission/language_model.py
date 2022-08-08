import pickle
import sys

# --------------------------------------------------------------------------
# \                                  MAIN                                  \
# --------------------------------------------------------------------------


NnGram = 4
smoothingType = 'K'
inputFilePath = "./corpus.txt"
if (len(sys.argv) == 1):
  NnGram = 4
elif (len(sys.argv) != 4):
  print('Usage: \n language_model.py <n_value, default=4> <smoothing type, default=K> <path to corpus, default="./corpus.txt">')
  exit()
else:
  NnGram = int(sys.argv[1])
  smoothingType = sys.argv[2]
  inputFilePath = sys.argv[3]

# corpus = open("./corpora/test.txt", "r", encoding="utf-8")
corpus = open(inputFilePath, "r", encoding="utf-8")
outputModelFile = open("./model.pkl", "wb")
outputTextFile = open("./model.txt", "w")

model = {}
while True:
  toks = corpus.readline()
  if toks == "":
    break #EOF
  toks = toks.split()
  for j in range(1,NnGram+1):
    for i in range(j,len(toks)+1):
      # print(i-j, i)
      toksN = tuple(toks[i-(j):i])
      print(toksN, end=': ')
      if toksN in model:
        model[toksN] += 1
      else:
        model[toksN] = 1
      print(model[toksN])

outputTextFile.write(str(model))
pickle.dump(model, outputModelFile)
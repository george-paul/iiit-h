import re           # regex
import sys          # for command line args

# --------------------------------------------------------------------------
# \                                  MAIN                                  \
# --------------------------------------------------------------------------

if (len(sys.argv) > 1):
  inputFilePath = sys.argv[1]
else:
  inputFilePath = "./corpora/general-tweets.txt"

# tweetsCorpus = open("./corpora/test.txt", "r", encoding="utf-8")
tweetsCorpus = open(inputFilePath, "r", encoding="utf-8")
outputFile = open("./2021121006_tokenize.txt", "w", encoding="utf-8")

# Special placeholders:
# <NUM> - eg. "1", "2", "45", "1947"
# <PCT> - eg. "25%", "127%"
# <TIME> - eg. "17:30" , "2:30pm" 

while True:      # while the tweets corpus has lines left
  words = tweetsCorpus.readline()
  if words == "":
    break
  words = words.split()
  toks = []
  
  for word in words:
  
    # Hashtags
    if re.search(r"[#]\w{1,}", word) != None:
      toks.append("<HASHTAG>")
      continue
  
    # Mentions
    if re.search(r"[@]\w{2,}",word) != None:
      toks.append("<MENTION>")
      continue

    # URLs
    if re.search(r"https{0,}://",word) != None:
      toks.append("<URL>")
      continue
    if re.search(r"\w+\.\w{2,}",word) != None:
      toks.append("<URL>")
      continue

    # Time
    if re.search(r"(\d{1,2}:\d{2})([ap]m){0,}",word) != None:
      toks.append("<TIME>")
      continue

    # Percentages
    if re.search(r"\d+%",word) != None:
      toks.append("<PCT>")
      continue

    # Numbers
    if re.search(r"\d+",word) != None:
      toks.append("<NUM>")
      continue
    
    # Contraction
    if re.search(r"[A-Za-z]{2,}'[A-Za-z]+", word) != None:
      temp = word.split("'")
      toks.append(temp[0].upper())
      toks.append("'" + temp[1].upper())
      continue

    # toks.append(word)        # DEBUG

    # split punctuation
    puncOrWord = re.split(r"(\W+)", word)
    for pw in puncOrWord:
      if re.search(r"(\W+)", pw) != None:
        temp = re.findall(r"(\S)\1*", pw)
        tempNext = ""
        for t in temp:
          tempNext += t
        toks.append(tempNext)
      elif pw == '':
        continue
      else:
        toks.append(pw.upper())
  
  for word in toks:
    outputFile.write(word+" ")
    print(word, end=' ')
  outputFile.write("\n")
  print("")
# README - NLP assignment 3

### Train

To train the model run

```
python3 ./train_model.py
```

with the corpus in `./europarl-corpus/train.europarl`



### Probability Calculation

Run the probability calculation with

```
python3 ./language_model.py ./modeltf
```



### Generate Perplexities

Generate `2021121006_LM_train.txt` with 

```
python3 ./gen_perps.py ./modeltf
```


# Natural Language Inference 
`Also known as Recognizing Textual Entailment` is the task of determining whether a given sentence called Hypothesis is entailed/contradicted/neutral by a given premise.

## Datasets used
1. [SNLI](https://nlp.stanford.edu/projects/snli/) - Stanford Natural Language Inference Dataset
2. [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/) - Multi-Paradigm Natural Language Inference Dataset

These can also be accessed at the this [link](https://drive.google.com/drive/folders/1-Vs5L21uy8XIyztOSi39xfFBNQ9bBgO6?usp=sharing) along with GloVe Embeddings that were used.

## Models
We made nine neural network models in total for the task. Ranging from the simplest to the most complex using `LSTM`, `GRU` and `BERT`.
<br>
We also tinkered around with the activations of the neurons and tried to find the best combination of them to get the best results. We used the following activations:
<br>
1. `Sigmoid`
2. `ReLU`
4. `Softmax`

All the models can be found at this [link](https://drive.google.com/drive/folders/1aVH60cTMMR9f_VWp6gjxClxkoOslX0oY?usp=sharing).

## Running the code
To run the code, you need to install the following packages:
<br>
1. `pip install transformers`
<br>

Now you can run the code directly using the given python notebooks after downloading the dataset and GloVe embeddings from the given links.
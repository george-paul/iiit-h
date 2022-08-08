# Intro to NLP - Project Outline

**Team:** 32 - NAGin

**Team Members:** George Paul, Amal Sunny, Nukit Tailor 

## About the Project

Natural Language Inference (NLI), also known as Recognizing Textual Entailment is the task of determining the inference relation between two (short, ordered) texts: *entailment*, *contradiction*, or *neutral*. 

Our task is to identify whether a given hypothesis(H) can be inferred from textual statement(T). The model will classify these pairs in three classes:

* Contradiction - The text implies the exact opposite of the hypothesis. If the meaning inferred from the text is just the opposite of the meaning conveyed in the hypothesis, then the text-hypothesis pair is contradictory. For example, 

  > T - "The man ate a red apple"
  >
  > H - "The man never eats fruit"

* Entailment - The text entails the hypothesis if the hypothesis infers its meaning from the text.
  For example,

  > T - "The man ate a red apple"
  >
  > H - "The man eats fruit"

* Neutral - If there is no inferred information present in the hypothesis, the text-hypothesis pair remains neutral.
  For example, 

  > T - "The man ate a red apple"
  >
  > H - "An apple fell on Issac Newton"







## Scope

The scope of the project is to take a set of Text-Hypothesis (T-H) pairs and using a language model, powered by a machine learning based neural network implementation, will classify the set into three classes namely: into Contradiction, Entailment and Neutral pairs.
The model will be trained mainly using the Stanford Natural Language Inference dataset and MultiNLI dataset which has pairs of Texts and Hypotheses that have been marked by five people with judgments as to whether or not the text entails the hypotheses, or contradicts. If neither, then a neutral judgment is given. The pair will then be marked with consensual judgment of the five people.

## Implementation Plans

Implementing this project involves a great amount of knowledge and research. The project will progress in several stages.
The first stage towards developing this model is to find and expand on existing research. The team will scour the Internet for relevant papers and read and comprehend them.
The next stage is to gather this knowledge and start working towards a bare-bones prototype of the final software. Conducting some initial testing will be paramount to the success of the final result.
Next, comes the training and fine tuning of the parameters of the model so as to obtain the highest possible accuracy and precision.

Finally, the model is tested on datasets separate from the training set and final scores for accuracy are tallied so that the team can report on the success of the project.
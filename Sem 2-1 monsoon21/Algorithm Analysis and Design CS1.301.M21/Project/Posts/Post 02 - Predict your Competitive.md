# Predict your Competitive Exam Results with this one Simple Trick!

*You're totally Rank 1, I'm telling you*



***



Picture this - You've just given the JayYeeYee, a competitive exam for entrance into the top clown colleges in the country. And of course, as a hopeful clown, you want to know how you compare with your fellow aspirant antics. You go around asking all your friends and some strangers - "Hiya! How was your exam? How much do you think you'll get?".
You get many varied answers. The JayYeeYee features negative marking for wrong answers so there are some candidate comedians who joke "I was better off not writing this exam!" and then there are other professional pranksters who say "This exam was pretty easy right?". I bet you're confused as to how one can predict this result. Well, there's an algorithm for that!

## The Setup

The rank based nature of the exam means that only the top 150 ranks get into the prestigious AIAIT (All India Academic Institute of Trickery). You also know that around 750 candidates write this exam. So that's a top 20% cut-off, rather exclusive but not beyond reach. You have a sample of 19 friends and yourself whose scores you have in an unsorted list. The top 20%, or equivalently the 80th percentile score, would be the 4th highest score in your list. Your hopes wear thin but you can't let this go and you think about it every night. The anxiety gets to you and you decide to get to the bottom of it. Introducing the Median of medians algorithm.

## The Idea

You realise that sorting and then counting down to find the 4th highest score is wildly inefficient.

> Note to reader: In this particular case it really isn't too inefficient. For this 20-sized input there's no real, wrong way to do it but for the purposes of introducing the algorithm, we'll assume that the input is too large for naïve algorithms like the one I just mentioned.

So what's the plan?

As with most problems in the STEM fields, and as with military and political scenarios (generally a useful way of thinking really), we will _divide and conquer_.

Observe the following:

* We know that sorting a constant sized list, of say 5 items, is quick.
* Finding the median of the list of 5 items is also very quick since we can just access the third item directly.
* Finding the median of a list which is smaller than another list will be quicker.

The plan is then, to divide the list into smaller lists of 5 items each. And operate on each of them and use them to form a final answer.
This strategy is famous and useful among algorithm designers, especially, since the prospect of doing the same thing over and over again within itself is easy for computers and it's called recursion. And if we can somehow make the problem smaller each time then there's eventually going to be an answer at the end of it all. 

The process of recursion is when a procedure uses the procedure itself as a step in the procedure. It sounds rather complex but think of it like Russian matryoshka dolls. The important part is that eventually there's an end to it.

![matryoshka](Assets/Post 02 - Predict your Competitive/matryoshka.gif)

## The Algorithm

The algorithm takes in `L`, the list that needs to be sorted, and `i`, which indicates that it returns the `i`th smallest element. Our requirement, to estimate our JayYeeYee results, actually asks for the 4th _largest_ number. This is actually no different from the 17th _smallest_ (17 = 20-4+1).

```
medianOfMedians(L,i):
```

As was the plan, the first step is to divide the list into smaller ones of a constant size (we've chosen 5 for no particular reason other than the fact that it's odd so we'll have a nice clean element in the centre for the median). `sublists` is a list of the sublists.

```
For every fifth j do:
	Append a list containing L[j to j+5] to sublists
```

Now we find the median of each sub-list. Usually it's a good idea to use the in-built sorting function for the programming language you're using or write your own mergesort/quicksort function (Further reading: Or if the conditions match then maybe [Counting Sort](https://en.wikipedia.org/wiki/Counting_sort)). Add each median to a new list named `medians`.

```
Sort each sublist
For each sublist:
	Append sublist[length(sublist)/2] to medians
```

Here comes the smart part that saves us a ton of time. Next, find the median of the `medians` sub-list. But... isn't that our problem in the first place? YES EXACTLY. We're recursing. We can do a little check to see if the length of the `medians` sub-list is less than 5, in which case we can do our quick, little sort-and-take-the-middle-item manoeuvre. If not, then we do the whole algorithm on the (guaranteed to be smaller than our original list) `medians` sub-list.

```
If length(medians) <= 5 then:
	Sort medians
	pivot = medians[length(medians)/2]
Else:
	pivot = medianOfMedians(medians, length(medians)/2)
```

But Mr. AlgorithmsMan, what's this `pivot`? Wonderful question.
The next step is to partition the veritable sea of elements we have in our original list into two - the ones that are greater than, and ones that less than the `pivot`. `hi` and `lo` respectively.

```
For every element l in L:
	If l > pivot, append l to hi
	Else if l < pivot, append l to lo
```

Algorithms Magic Part 2: We now have two lists that are definitely greater than and less than an approximate median we've called the `pivot`. Suppose the `i` we gave our algorithm was 5, that is, we wanted the 5th smallest element in the list.  If the length of the list `lo` is equal to four, then we have our answer in `pivot`! Else we know that `pivot` has exactly `length(lo)` elements less than it. And thus is the `length(lo)+1`th smallest element in the list `L`. If the required `i`th smallest element is less than `length(lo)+1` then we do the whole thing all over again with the smaller, partitioned list `lo`. And likewise if `i` is larger than `length(lo)+1` we do the same thing, but this time, with `length(lo)+1` elements cut off, `i` becomes `i-(length(lo)+1)`

```
If length(lo)+1 == k then:
	return pivot
Else If length(lo)+1 < k then:
	return medianOfMedians(lo, i)
Else length(lo)+1 > k then:
	return medianOfMedians(lo, i-(length(lo)+1))
```

And that concludes the algorithm!

## Why does it work?

A rigorous proof of why this algorithm works is beyond the scope of this article (and indeed the whole series doesn't intend to go into that much depth). The gist of it is that every time we partition the list, we are surely making progress towards an answer since we're cutting out definite non-answers.

Another question you might have is, wouldn't we definitely make progress regardless of the choice of `pivot`? Well, yes actually. But the problem is that the progress made each time is dependent on the partition being made. Sure, choosing a pivot that cuts off a large majority of the list would be ideal. But in the worst case (which is the case in which algorithms are evaluated incidentally) we cut off one element at a time. This is no better than sorting the list and choosing the `i`th element, an approach we already ruled out.



***



Having learned the working of the Median of Medians algorithm, maybe some further reading is needed for the especially hungry learner (which you hopefully are!):

* [Wikipedia](www.wikipedia.org/wiki/Median_of_medians) is often a good place to start, but almost never a good place to end your learning.
* [A nice lecture from MIT OCW](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/lecture-videos/lecture-2-divide-conquer-convex-hull-median-finding/) that goes into greater depth about median finding.
* [A video lecture on the randomized variant from NPTEL](https://www.youtube.com/watch?v=Wo5sBYiaGns) for those of you who are convinced we can do better.



Alright! So how does it feel knowing the fate of your career in jestership? Hopefully a weight has been lifted off your chest and you can look forward to a good night's sleep.


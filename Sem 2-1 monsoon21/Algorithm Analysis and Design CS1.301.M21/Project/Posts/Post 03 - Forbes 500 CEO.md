# Fortune 500 CEO reveals her Productivity Secrets

_You're definitely not as busy as her, But you still gotta read this._



***



This blog's correspondents have recently struck gold. An interview and window into the life of the CEO of a company on Fortune's 500 largest companies in America. She will remain unnamed at her request and will be referred to as K for the rest of this article.

## Who are you?

K is a motivated, successful businesswoman, mother and leader who describes herself as both the cautious, calculated voice in decision making but also one who often introduces wild, wacky risks that, to her credit, have mostly paid off. She manages the company C which is a nationally recognizable brand, depended on by  millions and employing over 200,000 people.

![img](Assets/Post 03 - Forbes 500 CEO/Female-CEO.jpg)

*This isn't her, it's just a nice picture (Source: [onlinemasters](https://onlinemasters.ohio.edu/blog/ceo-vs-owner/))*

**Interviewer: **How do you handle the responsibilities of being in such a position?

**K: **It's very simple - I don't! There's throngs of people who think I'm some superhuman who manages and handles all sorts of decisions every day with the sole responsibility hanging on me. This is just false. 
A company this large is made up of _at least_ 1,000 management personnel. And another 100,000 people doing the work. There's no reason for me to shoulder that large a responsibility. We are a team and the thought and consequences that go into any decision we make are shared by around 50 people each time. Of course, often I'm the largest and some would say "most important" voice at the table but I like to think of myself as another cog in the system.

## The Secrets

**Interviewer: **You described yourself as a very communicative leader. Most employees and people in the workforce tend to dislike meetings. What's your attitude towards them?

**K: **Depends on the people and the subject. I am usually scheduled for more meetings than there is time in the day! So it does get monotonous sometimes. But I never dislike them. Being a part of the process and giving my input and ideas is the one thing I'm good at and by golly I will do it!

**Interviewer: **You mentioned that your schedule has more meetings than you have time for in the day. How do you manage that?

**K: **Okay so I'm often invited to meetings that overlap and conflict but obviously there's no way to be in two meetings at a time and be fully present in both. The _secret_ is this: Attend as many as possible! You'll be surprised how motivated and energized employees are when you, the CEO, come to attend a meeting about the smallest thing! The way I do that is by attending the highest number possible and thus interacting with as many people as I can. Early on, during my college education as a computer science engineer, I came across this wonderfully simple but entirely thorough algorithm that helps me daily in planning my day. It's called the Activity Selection Algorithm and allow me to introduce you to it...



The Activity Selection algorithm is the solution to a problem that's usually posed in this way:

An auditorium owner charges $100 for each booking made to his auditorium. Obviously being a business owner, they wants to maximize profits for each day by maximizing the number of bookings.
They has a list of requests at the start of each day - each with a time at which the booking starts a the time at which it ends. Something that looks like:

```
A[i] =   0   1   2   3   4
S[i] =   4   0   2   1   3
E[i] =   6   2   3   6   4

Time =   0   1   2   3   4   5   6
		 |---1---|-2-|-4-|---0---|
		     |---------3---------|
```

Pretty much what this means is that, Activity `0` Starts at time `4` and Ends at time `6`. And so on for the rest. Now the task is to choose some of the activities (that is, choose some `i`s) such that there are no overlaps and that the chosen list has the highest number of activities possible.

## Smart Work not Hard Work

Trying out every possible combination, checking whether it's valid and then recording its length, at the end comparing between them to find the largest. It's just not good enough.

The main emotion behind the solution to this problem is _greed_. We want _as many_ activities as possible. The main resource here is time and we want to be as greedy as we can with it. The first thought, usually, is to assign activities that we know take up the least amount of time. And was indeed my first thought when approaching the problem. It's important to tell you why this doesn't work since it kinda goes against normal intuition.

Consider this example input:

```
A[i] =   0   1   2
S[i] =   0   2   3
E[i] =   3   4   6

Time =   0   1   2   3   4   5   6
		 |-----0-----|-----2-----|
		         |---1---|
```

According to our intuition, we choose `A[1]` since that activity takes up only `4-2=2` hours of the auditorium's time. But notice that, due to an overlap, that immediately rules out the other two activities which could've both been scheduled for a higher number of bookings. 

Let me tell you how it's actually solved now - Imagine your auditorium was open for only 3 hours, from `0` to `3`. The one and obvious scheduling would be activity `0`. Now imagine it was only open from `3` to `6` and now the only, obvious scheduling is activity `2`. This is how we'll approach the whole thing.
Cut off a certain part of the time from the start by choosing the activity(booking) that ends at the earliest time so that we can have the most amount of time left to schedule more bookings. At every step we approach the problem with this stingy attitude towards giving away time to activities. If the earliest end time is `3` then we are being greedy in that we want to schedule the very next `3` hours with this activity exactly. This approach is why the algorithm is called a *greedy* algorithm.

## How does she do it then? 

Written down the algorithm looks like this:

Given a list of Activities `A`, and a list of start and end times for those activities `S` and `E`, `ActivitySelection` gives a list which is a subset of `A` which is scheduled with the highest number of activities without conflicts.

```
ActivitySelection(A,S,E):
```

To readily choose the activities according to their end time we'll sort them.

```
Sort A according to the corresponding end time in E
```

Create a new list that will eventually contain our final answer `Selected`, and append the activity with the earliest finish time, that is the first one in the sorted `A`. Also keep track of the latest activity added to `Selected` with `k` as we add them in the next step

```
Append A[0] to Selected
k = 0
```

Check each activity in the order specified by `A`, If the activity doesn't overlap with the latest activity added to `Selected` then add it to `Selected`. And finally, after going through the whole list `A` return the list `Selected` as the output.

```
For each i from 0 to length(A):
	if S[i] >= E[k] then:
		Append A[i] to Selected
		k = i
Return Selected
```

## So that's how she does it

**Interviewer: **Wonderful! So using this algorithm you always manage to attend as many meetings as possible. Although, Tell me - how do you manage to contribute well on each of the meetings you attend?

**K: **You say "contribute" like I'm the one coming up with everything. The best thing you can do during a discussion is to listen well. While deciding, say the fate of a new design, I don't operate purely on instinct or opinion. What I do is, I listen to my team and imbibe the things they have to say and operate on those assumptions and ideas. That's also one way to chose good employees! Pick the ones that aren't afraid of putting their ideas out there.



***



Having heard from such a reputed manager in a position of such high authority, it makes you think anyone can do well in such a circumstance given some wit, confidence and dedication to the cause. Thank you to K for giving us these valuable insights!

> Disclaimer: In reality, No CEO, from a Fortune 500 company or otherwise, was involved in the making of this article. This is mostly the work of a dude at his computer who's rather bored.

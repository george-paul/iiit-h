# Honours Project 1 - Report



### Outline

Under the supervision of Dr. Bhaktee Dongaonkar and with the CogSci lab, the project I've undertaken is to develop a digitised version of the [Neuro-Cognitive Tool Box](http://brandp.in/icmr/index.html), a batter of cognitive tests published by the Indian Council of Medical Research. After development, the project will also involve quantifying the differences between the physical pen-and-paper test and the digitised version.



### Progress

Digitisation has begun in the form of a mobile application written using the Flutter framework. The over-arching layout and common components for the app have been created and individual test digitisation has begun.

At the time of writing this report, three tests out of a potential eleven tests in the NCTB have been digitised:

1. Picture Naming Test
2. Trail Making Test B & W (A & B)
3. Category Fluency



### Potential Roadblocks

- For tests requiring verbal answers from the patient in the physical versions of tests, the corresponding digitisation has proven to be problematic. Although recording and storing verbal answers from users is already incorporated into the app, automatic evaluation by means of current speech-to-text technology is unreliable.
- Backend tech stack for the application consists entirely of Google's Firebase service at the moment. This can't be the case for the final version. A transition to a self-hosted backend will be needed. A potential solution is to migrate the backend to a self-hosted instance of [supabase](https://supabase.com/).
- The current digitisation of the Trail Making Test is in no way responsive to screen size changes. In the event that users take the test on devices with varying screen, scores will be skewed according to the changes in screen size versus the current baseline (a 26.2cm diagonal screen).
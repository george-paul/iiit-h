/- A basic lean assignment. This assignment is partly to test what you learnt in lecture 3, and partly to test your ability to learn lean from the documentation.

A note: You will see that this assignment has been uploaded within a lean project. This is because the lean ecosystem uses projects to install libraries locally- much the same way python uses `venv`- and for this assignment, you will need the lean library `mathlib`. For _that_ you need to install the lean project manager.

Install instructions for the lean project manager `leanproject` are here: https://leanprover-community.github.io/install/debian_details.html 

Going on to the actual assignment -/

import data.rat

/- (1) Define an inductive `even` function (write the inductive cases for the helper function) -/
def evenOddHelper: bool -> ℕ -> bool
  | tt 0 := tt
  | ff 0 := ff
  | tt (x+1) := evenOddHelper ff x
  | ff (x+1) := evenOddHelper tt x

def myeven : ℕ -> bool := evenOddHelper tt

/- (2) Define the function `power : ℕ -> ℕ -> ℕ` inductively. Suggestion: look at how [multiplication is defined in lean](https://github.com/leanprover-community/lean/blob/e69ab934262eb6f141344fdaec98ede68a9102b6/library/init/data/nat/basic.lean#L34) -/


-- Now we can define this as an infix operator:
def power: ℕ -> ℕ -> ℕ
  | a 0 := 1
  | a (b + 1) := (a * (power a b))

/- (3) Define a function that outputs the derivative of a function w.r.t some interval - df(x) = d/dx (f) - using a function  `f` passed as argument. The type of the function `df` is given for you, as are a series of test cases -/
def k : ℚ := 1/2000
-- #print k
def df (f : ℚ -> ℚ) : (ℚ -> ℚ) :=
  λx : ℚ, (f (x + k) - f (x)) / k

def f1 (x : ℚ) := x*x + 1
def df1 := df f1
#check df1
-- answer: df1 : ℚ → ℚ
#eval df1 1000
-- answer: 4000001/2000


/- Note: for this one, you need to use the rational number type ℚ . Notice the import at the top of the file- we're importing rationals from lean's basic math library `matlib`. Try compiling the following to get a feel for using rationals: -/
def z : ℚ := 1.234
#print z

/- So this is the type for rational numbers (floats are currently experimental in lean, so I'd suggest using rationals) and this is how they're represented -/

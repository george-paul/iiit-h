/- The syntax of propositional logic expressions is defined here in lean (along with a few helpful operators) -/

namespace hidden

structure var :=
mk :: (idx : ℕ) 

inductive Expr
| atom (v : var) : Expr
| not  : Expr -> Expr
| and  : Expr -> Expr -> Expr
| or   : Expr -> Expr -> Expr
| impl : Expr -> Expr -> Expr

prefix `atom` : 49 := Expr.atom
prefix `¬`    : 50 := Expr.not
infix `Λ`     : 51 := Expr.and
infix `V`     : 52 := Expr.or
infix `⇒`     : 53 := Expr.impl


/- Q1: This question is a warm-up to using propositions inductively. Define a function `size` that returns the size of the propositional logic expression -/


def size : Expr -> ℕ
  | ¬a := size(a) + 1
  | (a Λ b) := size(a) + size(b) + 1
  | (a V b) := size(a) + size(b) + 1
  | (a ⇒ b) := size(a) + size(b) + 1
  | _ := 1

/- Q2. Now we get into a bit of an open area. Remember the definitions of an `interpretation` and a `valuation` that we did in class.

How would you build propositional logic syntax and semantics in lean, such that you can have a function `valuation : Expr x Interpretation -> bool` - that takes a type `Expr` - your type for propositional expressions ; a type `Interpretation`, and returns a boolean?

(Note: your `valuation` function does not need to be exactly this type! What this question asks of you is to implement propositional logic syntax and semantics in a way that supports a mechanism for defining expressions, defining interpretations and computing valuations on the expressions x interpretations)  

To see what "building propositional logic" means, you could refer to the propositional logic syntax I built in [the Propositions In Lean tutorial notes](../../tutorial-notes/propositions-in-lean.org). -/


structure inter :=
mk :: (idi : ℕ) (val : bool)

-- def i1 := inter.mk 1 tt
-- #eval i1.idi

def getIdx : Expr -> ℕ
  | (Expr.atom v) := v.idx
  | (¬e1) := getIdx e1
  | (e1 Λ e2) := max (getIdx e1) (getIdx e2)
  | (e1 V e2) := max (getIdx e1) (getIdx e2)
  | (e1 ⇒ e2) := max (getIdx e1) (getIdx e2)

def value : list inter -> ℕ -> bool
  | (a::l) n := if a.idi=n then a.val else value (l) (n)
  | [] n := ff

def valuation : list inter -> Expr -> bool
  | i (e1 ⇒ e2) := (bnot (valuation (i)  (e1))) || (valuation (i)  (e2))
  | i (e1 V e2) := (valuation (i)  (e1)) || (valuation (i)  (e2))
  | i (e1 Λ e2) := (valuation (i)  (e1)) && (valuation (i)  (e2))
  | i (¬e) := bnot (valuation i (e))
  | i (e) := value i (getIdx e)


def e1 : Expr := Expr.atom(var.mk 1)
def e2 : Expr := Expr.atom(var.mk 2)
def e3 : Expr := e1 V e2
def li : list inter := [inter.mk 1 ff, inter.mk 2 ff, inter.mk 3 tt]

#eval valuation li e3

/- Q3. Can you implement a type `is_sat (e : Expr)? Implement it as a record type (remember `vector` from the class notes) -/

end hidden

-- def add (a : ℕ) (b : ℕ) : ℕ
--   := a + b

-- -- -- constant addType (p : ℕ) (q : ℕ) : ℕ

-- -- def incr : ℕ → ℕ := 
-- --   add 1

-- -- def mul (c : ℕ) (d : ℕ) : ℕ 
-- --   := c * d

-- -- ---------------------- list indexing -----------

-- -- open list

-- -- #check nth

-- -- def ls := [1,2,3]

-- -- constant tensor : list (list (list ℕ))
-- -- #check tensor

-- -- def index (y : ℕ) (x : ℕ) (z : ℕ) : ℕ :=

-- -- #eval nat.succ(2)

-- -- def fact : ℕ → ℕ
-- --   | 0 := 1
-- --   | (n+1) := (n+1) * fact(n)

-- -- def fact : ℕ → ℕ
-- --   | 0 := 1
-- --   | n := n * fact(n-1)

-- open nat

-- def fact : ℕ → ℕ
--   | 0 := 1
--   | (succ n) := (succ n) * fact(n)

-- #eval fact(5)

-- def succ : ℕ → ℕ 
--   | n := n + 1


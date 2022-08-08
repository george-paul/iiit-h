
/- Remove the placeholder and complete the following proofs -/
open classical

variables A B C : Prop
variables p q r : Prop

-- 1
example : A ∨ B → B ∨ A := 
begin
	intro h,
	cases h with ha hb,
	{
		right,
		assumption,
	},
	{
		left,
		assumption,
	},
end

-- 2
example : A ∧ (B ∨ C) → (A ∧ B) ∨ (A ∧ C) :=
begin
	intro h,
	cases h with ha hbc,
	cases hbc with hb hc,
	{
		left,
		split,
		{apply ha,},
		{apply hb,},
	},
	{
		right,
		split,
		{apply ha,},
		{apply hc,},
	},
end

-- 3
variables X Y Z: Prop
theorem not_f : (¬X) = (X → false) := rfl
example : ¬(A ∨ B) ↔ ¬A ∧ ¬B := 
begin
	repeat {rw not_f},
	split,
	{
		intro h,
		split,
		{
			intro a,
			apply h,
			left,
			apply a,
		},
		{
			intro b,
			apply h,
			right,
			apply b,
		},
	},
	{
		intro h,
		cases h with af bf,
		intro ab,
		cases ab with a b,
		{apply af, apply a,},
		{apply bf, apply b,},
	},
end

-- 4
theorem not_not : ¬¬X ↔ X :=
begin
	split,
	{
		intro hnnx,
		by_contradiction,
		contradiction,
	},
	{
		intro hx,
		by_contradiction,
		contradiction,
	},
end

theorem imp_to_or : X → Y ↔ ¬X ∨ Y := 
begin
	split,
	{
		intro xiy,
		by_cases X,
		{
			right,
			apply xiy,
			apply h,
		},
		{
			left,
			apply h,
		},
	},
	{
		intro xoy,
		intro x,
		cases xoy,
		{
			contradiction,
		},
		{
			apply xoy,
		},
	},
end

theorem nximpny : ¬X -> ¬Y ↔ Y → X :=
begin
	split,
	{
		intro h,
		rw imp_to_or at h,
		rw not_not at h,
		rw or.comm at h,
		rw ← imp_to_or at h,
		apply h,
	},
	{
		intro h,
		rw imp_to_or at h,
		rw or.comm at h,
		rw ← not_not X at h,
		rw ← imp_to_or at h,
		apply h,
	},
end

example : ((p → q) ∧ (¬r → ¬q)) → (p → r) := 
begin
	intro h,
	cases h with pq rq,
	intro p,
	rw nximpny at rq,
	apply rq,
	apply pq,
	apply p,
end
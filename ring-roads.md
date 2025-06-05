Here is a single copyable plain-text block from the selected pages of the paper. It has been cleaned and reformatted for clarity and optimal comprehension by a large language model (LLM). All equations and symbols are expressed in a machine-readable textual format:

⸻

Emergency Service Location Problem with Ring Roads

Problem Description

Assume there are m callers, each located at a fixed point Y_i, for i ∈ M = {1, ..., m}. These callers are served by n emergency service centers S_j, for j ∈ N = {1, ..., n}. Each service center S_j must be placed on a given simple closed curve D_j. Without loss of generality, each D_j is modeled as a circle of circumference d_j.

Each D_j has two exits A_j and B_j, placed at opposite ends of a diameter, such that the arc |A_j B_j| = d_j / 2. Let a_ij be the distance from Y_i to A_j, and b_ij the distance from Y_i to B_j. These are known distances.

Let x_j be the position of the service center S_j on D_j, measured as the length of the directed arc from A_j to S_j in the counterclockwise direction. Thus x_j ∈ [0, d_j).

Two cases arise:
	•	If x_j ≤ d_j / 2, then the available routes from S_j to Y_i are:
	•	S_j → A_j → Y_i with total length x_j + a_ij
	•	S_j → B_j → Y_i with total length d_j / 2 - x_j + b_ij
	•	If x_j > d_j / 2, then the available routes from S_j to Y_i are:
	•	S_j → A_j → Y_i with total length d_j - x_j + a_ij
	•	S_j → B_j → Y_i with total length x_j - d_j / 2 + b_ij

Define four route distance functions:

r₁(x_j) = x_j + a_ij              for x_j ∈ [0, d_j / 2)
r₂(x_j) = d_j / 2 - x_j + b_ij    for x_j ∈ [0, d_j / 2)
r₃(x_j) = x_j - d_j / 2 + b_ij    for x_j ∈ [d_j / 2, d_j)
r₄(x_j) = d_j - x_j + a_ij        for x_j ∈ [d_j / 2, d_j)

The actual distance r_ij(x_j) from S_j to Y_i is:

r_ij(x_j) = min { r₁(x_j), r₂(x_j), r₃(x_j), r₄(x_j) }

Assuming each caller is served by their nearest center:

min_{j ∈ N} r_ij(x_j) = r_it(x_t)   for some t ∈ N

The overall objective is to minimize the maximum of the minimum distances:

f(x₁, ..., x_n) = max_{i ∈ M} min_{j ∈ N} r_ij(x_j)

A threshold α may be imposed to ensure a service quality guarantee:

f(x₁, ..., x_n) ≤ α

Define the feasible location set:

L(α) = { (x₁, ..., x_n) | 0 ≤ x_j ≤ d_j, ∀ j ∈ N and f(x₁, ..., x_n) ≤ α }

Formally, the optimization problem is:

P1:
  minimize f(x₁, ..., x_n)
  subject to (x₁, ..., x_n) ∈ L(α)
             0 ≤ x_j ≤ d_j for all j ∈ {1, ..., n}


⸻

Reformulated Optimization Problem

Under Assumptions 1 and 2, the problem can be reformulated as:

P2:
  minimize   f(x₁, ..., x_n)
  subject to L(α) ≠ ∅

Inputs and Outputs

Inputs:
	•	Number of callers m at fixed positions Y_i
	•	Number of service centers n
	•	Distance a_ij from Y_i to exit A_j, ∀ i ∈ M, j ∈ N
	•	Distance b_ij from Y_i to exit B_j, ∀ i ∈ M, j ∈ N
	•	Circumference d_j of ring D_j, ∀ j = 1,…,n
	•	Optional distance threshold α̃

Outputs:
	•	Optimal value of α
	•	Optimal positions x_j^opt

Algorithm for Solving Problem P2
	1.	Check Assumption 1. If invalid, stop.
	2.	For each i ∈ M, j ∈ N, compute δ_ij = min{a_ij, b_ij}
	3.	For each i, compute α̃_i = min_j δ_ij; set α̃ = max_i α̃_i
	4.	If α is not given, set α = α̃; else proceed.
	5.	If α < α̃, stop (“infeasible”)
	6.	For all i, j, compute ρ_ij = max_x∈[0,d_j] r_ij(x)
	7.	For all i, j, compute boundary values:

μ*_ij(α)    = α - a_ij
μ**_ij(α)   = d_j - α + a_ij
ν*_ij(α)    = d_j/2 + b_ij - α
ν**_ij(α)   = α + d_j/2 - b_ij

	8.	Derive each V_ij(α) based on cases
	9.	For each i, find j(i) such that V_ij(α) ≠ ∅
	10.	Define P_j(α) = {i ∈ M | V_ij(α) ≠ ∅}
	11.	Compute V_j(α) = ⋂_{i ∈ P_j(α)} V_ij(α)
	12.	If all P_j(α) ≠ ∅, choose x_j^opt ∈ V_j(α); else choose x_j^opt ∈ [0, d_j)

Supporting Lemmas

Lemma 1:
Define

α̃_i = min_j δ_ij  
α̃ = max_i α̃_i  

Then the optimal solution is given by α̃.

Lemma 2:
If V_ij(α) ≠ ∅, then at least one of:
	1.	μ*_ij(α) = α - a_ij ≥ 0
	2.	μ**_ij(α) = d_j - α + a_ij ≤ d_j
	3.	ν*_ij(α) = d_j/2 + b_ij - α ≤ d_j/2
	4.	ν**_ij(α) = α + d_j/2 - b_ij ≥ d_j/2

Case Derivation for V_ij(α)

Assume a_ij > b_ij (Case 1(a)). Then:

δ_ij = b_ij  
ρ_ij = (d_j/2 + b_ij + a_ij)/2  

Define:

r₁(x_j) = x_j + a_ij
r₂(x_j) = d_j/2 - x_j + b_ij
r₃(x_j) = x_j - d_j/2 + b_ij
r₄(x_j) = d_j - x_j + a_ij

V_ij(α) is defined as:
	•	If α < δ_ij: V_ij(α) = ∅
	•	If α = δ_ij: V_ij(α) = {d_j/2}
	•	If δ_ij < α < a_ij:

V_ij(α) = [d_j/2 - (α - b_ij), d_j/2 + (α - b_ij)]


	•	If α = a_ij:

V_ij(α) = {0} ∪ [d_j/2 - (α - b_ij), d_j/2 + (α - b_ij)]


	•	If a_ij < α < ρ_ij:

V_ij(α) = [0, α - a_ij] ∪ [d_j/2 - (α - b_ij), d_j/2 + (α - b_ij)] ∪ [d_j - (α - a_ij), d_j)


	•	If α ≥ ρ_ij: V_ij(α) = [0, d_j)

Case 1(b) (when a_ij > b_ij > d_j/2):
	•	δ_ij = b_ij
	•	ρ_ij = d_j/2 + b_ij
	•	V_ij(α) = [d_j/2 - (α - b_ij), d_j/2 + (α - b_ij)]

Example Input

m = 5 neighborhoods  
n = 4 service centers  
d₁ = d₂ = d₃ = 22, d₄ = 16  
[(a_ij, b_ij)] =
[
  (3,3)   (9,10) (6,6)   (3,5)
  (4,6)   (8,9)  (7,8)   (5,6)
  (6,7)   (6,7)  (9,10)  (7,8)
  (7,7)   (5,6)  (3,2)   (9,10)
  (8,8)   (3,3)  (5,4)   (8,9)
]

Example Scenarios
	•	Scenario 1: No threshold α specified
	•	Scenario 2: α = 8
	•	Scenario 3: α = 5

⸻
Here is the final segment of the plain-text translation of the paper, preserving mathematical structure in a way that is readable by a language model:

⸻

Numerical Example Continued

The algorithm must first check if Assumption 1 is satisfied. In this example, it is satisfied. Then, proceed:

δ_ij = min(a_ij, b_ij) = 
[ [3, 9, 6, 3],
  [4, 8, 7, 5],
  [6, 6, 9, 7],
  [7, 5, 2, 9],
  [8, 3, 4, 8] ]

Compute:

α̃_i = (3, 4, 6, 2, 3)
α̃ = max(α̃_i) = 6

Scenario 1: No maximum threshold α given

Set α = α̃ = 6. Compute V_ij(6):

V_ij(α) = V_ij(6) =
[
  [ [0,3] ∪ [8,14] ∪ [19,22],  ∅,              {0,11},     [0,3] ∪ [7,9] ∪ [13,16] ],
  [ [0,2] ∪ {11} ∪ [20,22],     ∅,              ∅,          [0,1] ∪ {8} ∪ [15,16] ],
  [ {0},                        {0},            ∅,          ∅ ],
  [ ∅,                         [0,1] ∪ {11} ∪ [21,22],  [0,3] ∪ [7,15] ∪ [19,22], ∅ ],
  [ ∅,                         [0,3] ∪ [8,14] ∪ [19,22],  [0,1] ∪ [9,13] ∪ [21,22], ∅ ]
]

Each column j has at least one i with V_ij(6) ≠ ∅, satisfying feasibility. The feasible regions for the service centers are:
	1.	x₁ ∈ {0}: Place S₁ at exit A₁ for Y₁, Y₂, Y₃
	2.	x₂ ∈ {0}: Place S₂ at exit A₂ for Y₃, Y₄, Y₅
	3.	x₃ ∈ {0, 11}: Place S₃ at A₃ or B₃ for Y₁, Y₄, Y₅
	4.	x₄ ∈ [0,1] ∪ {8} ∪ [15,16]: Place S₄ at B₄ or near A₄ for Y₁, Y₂

Management decisions:
	•	2 centers: at {x₁, x₂}, {x₁, x₃}, or {x₂, x₄}
	•	3 centers: at {x₁, x₂, x₃}, {x₁, x₃, x₄}, or {x₂, x₃, x₄}
	•	4 centers: at {x₁, x₂, x₃, x₄}

The choice depends on factors like budget, expected call volume, and center capacity.

⸻

Scenario 2: α = 8

Since α = 8 > α̃ = 6, algorithm sets α = 6 → same result as Scenario 1.

⸻

Scenario 3: α = 5

Since α = 5 < α̃ = 6, proceed with α = 5:

V_ij(α) = V_ij(5) =
[
  [ [0,2] ∪ [9,13] ∪ [20,22],     ∅,          ∅,          [0,2] ∪ {8} ∪ [14,16] ],
  [ [0,1] ∪ [21,22],              ∅,          ∅,          {0} ],
  [ ∅,                           ∅,          ∅,          ∅ ],
  [ ∅, [0,2] ∪ [8,14] ∪ [20,22],  {0},        ∅ ],
  [ ∅, [0,2] ∪ [9,13] ∪ [20,22],  {0} ∪ [10,12], ∅ ]
]

Y₃ cannot be served within α = 5 ⇒ no feasible solution.

⸻

Conclusions and Future Directions

This work solves a class of n-emergency service location problems on ring roads.
	•	Service centers S_j must be located on arcs A_j B_j of circles D_j
	•	Given caller locations Y_i, distances a_ij and b_ij, and curve length d_j, the goal is to minimize:

f(x₁, ..., x_n) = max_i min_j r_ij(x_j)


	•	The model supports polynomial-time solution under two assumptions:
	1.	Distances (a_ij, b_ij) are nested
	2.	Feasible regions V_ij(α) are nested across i
	•	Applications include emergency service planning in new urban developments using ring roads

⸻

Let me know if you’d like a markdown or code-friendly version of the entire plain-text output.

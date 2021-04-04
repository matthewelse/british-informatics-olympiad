# Vision

This is a second round question, and this directory includes a few different
(equivalent) solutions to this problem: one brute force solution, and two greedy
algorithms. Included in this directory is a test to try and find examples where
the three solutions do not match up.

1. C++ solution: this is a brute force breadth-first search through the graph.
   It's fine on small inputs, but for anything larger, this quickly becomes too
   slow. Note that in the problem statement, it suggests that the number of
   telescopes and the number of walkers are each between 1 and 2^20, so this
   algorithm is very clearly not good enough.
2. Dynamic programming-ish solution: this exploits the "optimal substructure" in
   this problem. i.e. that to compute the largest score at telescope `k` after
   `n` steps, you just need to know the largest score for telescopes `k-1` and
   `k+1` after `n-1` steps.
3. Ad-hoc python solution. I've somewhat arbitrarily called this the "greedy
   solution" to distinguish it from the solution above. This solution uses the
   observation that optimal solutions will step along the path to a particular
   pair, and alternate between those two forever.

## Running the solutions

```bash
$ python vision_dynamic.py < large.in
666735333
$ python vision_greedy.py < large.in
666735333
$ clang++ vision.cpp && ./a.out < small.in
25
```

## Running tests

There are a few automated tests for this question.

```bash
$ export MACOSX_DEPLOYMENT_TARGET=10.15 # if you're running on mac os, and get build errors, you may need this
$ python test_vision.py
```

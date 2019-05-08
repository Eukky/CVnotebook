# Loop Invariants

## Overview

A loop invariant is a condition [among program variables] that is necessarilly true immediately before and immediately after each iteration of each loop.

The loop invariant must be true

1. before the loop starts.
2. before each iteration of loop.
3. after the loop teminater.

The loop invariant is always used for verifying algorithm correctness.

## Example

```cpp
int j = 9;
for(int i = 0; i < 10; i++)
    i--;
```

In the example it is true (for every iteration) that `i + j = 9`.

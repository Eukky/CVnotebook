# Insertion Sort

## Introduction

Insertion Sort is a simple sorting algorithm that builds the sorted array one item at a time. It is much less effcient on large lists than more advanced algorithm such as quick sort, heap sort, or merge sort.

## Time Complexity

$$ O(n^2) $$

## Advantage

- Simple implementation
- Efficient for small data sets, much like other quadratic sorting algorithms
- More efficient in pratice than most other simple quadratic $O(n^2)$ algorithms such as selection sort or bubble sort.
- Adaptive, efficient for data sets that are already substantially sorted: the time complexity is $O(kn)$ when each element in the input is no more than k places away from its sorted position
- Stable, does not change the relative order of elements with equal keys
- In-place, only requires a constant amount $O(1)$ of additional memory space
- Online, can sort a list as it receives it

## Pseudocode

```pseudocode
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
```

## Example

[Insertion Sort (CPP)](./SourceCode/InsertionSort.cpp)

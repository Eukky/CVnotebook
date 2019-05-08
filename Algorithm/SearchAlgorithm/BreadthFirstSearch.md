# Breadth-First Search

## Introduction

BFS is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

## Pseudocode

```pseudocode
1   Set all nodes to "not visited";
2   q = new Queue();
3   q.enqueue(initial node);
4   while (q != empty) do
5       x = q.dequeue();
6       if (x has not been visited)
7           visited[x] = true;
8           for (every edge(x, y))
9           if (y has not been visited)
10          q.enqueue(y);
```
# Red-Black Tree

## Properties

In addition to the requirements imposed on a binary search Tree, the following must be satisfied by a red-black tree:

1. Each node is either red or black.

2. The root is black.

3. All leaves(NIL) are black

4. If node is red then both its childern are black.

5. Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.

## Operations

- Rotate

```pseudocode
LEFT-ROTATE(T, x)  
//    y is the right child of x
01    y ← right[x]
02    right[x] ← left[y]
03    p[left[y]] ← x
04    p[y] ← p[x]
05    if p[x] = nil[T]
06        then root[T] ← y
07    else if x = left[p[x]]  
08        then left[p[x]] ← y
09    else right[p[x]] ← y
10    left[y] ← x
11    p[x] ← y
```

```pseudocode
RIGHT-ROTATE(T, y)  
//    x is the left child of y
01    x ← left[y]
02    left[y] ← right[x]
03    p[right[x]] ← y
04    p[x] ← p[y]
05    if p[y] = nil[T]
06        then root[T] ← x
07    else if y = right[p[y]]  
08        then right[p[y]] ← x  
09    else left[p[y]] ← x
10    right[x] ← y
11    p[y] ← x
```

- Insert

1. Add the node in a similar manner as a standard binary search tree insertion and color it red.

2. Fix up the red-black tree by series of operation such as rotation or coloring.

```pseudocode
RB-INSERT(T, z)  
01    y ← nil[T]
02    x ← root[T]
03    while x ≠ nil[T]
04        do y ← x
05        if key[z] < key[x]  
06            then x ← left[x]  
07            else x ← right[x]  
08    p[z] ← y
09    if y = nil[T]
10        then root[T] ← z
11        else if key[z] < key[y]
12            then left[y] ← z
13            else right[y] ← z
14    left[z] ← nil[T]
15    right[z] ← nil[T]
16    color[z] ← RED
17    RB-INSERT-FIXUP(T, z)
```

```pseudocode
RB-INSERT-FIXUP(T, z)
01    while color[p[z]] = RED  
02        do if p[z] = left[p[p[z]]]
03            then y ← right[p[p[z]]]
04                if color[y] = RED
05                    then color[p[z]] ← BLACK
06                    color[y] ← BLACK
07                    color[p[p[z]]] ← RED
08                    z ← p[p[z]]
09                else if z = right[p[z]]
10                    then z ← p[z]
11                    LEFT-ROTATE(T, z)
12                    color[p[z]] ← BLACK
13                    color[p[p[z]]] ← RED
14                    RIGHT-ROTATE(T, p[p[z]])
15            else (same as then clause with "right" and "left" exchanged)
16    color[root[T]] ← BLACK
```

- Remove

1. Remove the node in a similar manner as a standard binary search tree removing.

2. Fix up the red-black tree by series of operation such as rotation or coloring.

```pseudocode
RB-DELETE(T, z)
01    if left[z] = nil[T] or right[z] = nil[T]
02        then y ← z
03    else y ← TREE-SUCCESSOR(z)
04    if left[y] ≠ nil[T]
05        then x ← left[y]
06    else x ← right[y]
07    p[x] ← p[y]
08    if p[y] = nil[T]
09        then root[T] ← x
10    else if y = left[p[y]]
11        then left[p[y]] ← x
12    else right[p[y]] ← x
13    if y ≠ z
14        then key[z] ← key[y]
15        copy y's satellite data into z
16    if color[y] = BLACK
17        then RB-DELETE-FIXUP(T, x)
18    return y
```

```pseudocode
RB-DELETE-FIXUP(T, x)
01    while x ≠ root[T] and color[x] = BLACK  
02        do if x = left[p[x]]
03            then w ← right[p[x]]
04            if color[w] = RED
05                then color[w] ← BLACK
06                color[p[x]] ← RED
07                LEFT-ROTATE(T, p[x])
08                w ← right[p[x]]
09            if color[left[w]] = BLACK and color[right[w]] = BLACK
10                then color[w] ← RED
11                x ←  p[x]
12            else if color[right[w]] = BLACK
13                then color[left[w]] ← BLACK
14                color[w] ← RED
15                RIGHT-ROTATE(T, w)
16                w ← right[p[x]]
17            color[w] ← color[p[x]]
18            color[p[x]] ← BLACK
19            color[right[w]] ← BLACK
20            LEFT-ROTATE(T, p[x])
21            x ← root[T]
22        else (same as then clause with "right" and "left" exchanged)
23    color[x] ← BLACK
```

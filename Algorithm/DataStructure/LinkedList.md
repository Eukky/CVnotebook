# Link List

## Introduction

A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.

## Difinitions

```cpp
struct ListNode{
     int val;
     Node * next;
     ListNode(int x) : val(x), next(NULL) {}
 };
```

## Operations

- Insert

```cpp
void insertNode(ListNode *p, int i){
    ListNode* node = ListNode(i);
    node->next = p->next;
    p->next = node;
}
```

- Delete

```cpp
void deleteNode(ListNode *p){
    p->val = p->next->val;
    p->next = p->next->next;
}
```

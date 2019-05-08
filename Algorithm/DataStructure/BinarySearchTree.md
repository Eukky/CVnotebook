# Binary Search Tree

## Feature

- The value of left node is lesser than root.
- The value of right node is not greater than root.
- The left or right node must be a node of binary search tree.

## Definition

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x): val(x), left(NULL), right(NULL) {}
};
```

## Insert

```cpp
TreeNode* Insert(TreeNode* root, int val) {  
    if(root == NULL) {
        TreeNode* newNode(val);
        return newNode;
    }
    if(root -> val > val) {
        root -> left = Insert(root -> left, val);
    }else{
        root -> right = Insert(root -> right, val);
    }
    return root;
}
```

## Search

```cpp
TreeNode* Search(TreeNode* root, int val) {
    if(root == NULL) {
        return NULL;
    }
    if(root -> val == val) {
        return root;
    }
    if(root -> val > val) {
        return Search(root -> left, val);
    }
    return Search(root -> right, val);
}
```

## Inorder Traversal

```cpp
void Inorder(TreeNode* root) {
    if(root == NULL) {
        return NULL;
    }
    Inoder(root -> left);
    cout << root -> val << endl;
    Inoder(root -> right);
}
```

## Preorder Traversal

```cpp
void Inorder(TreeNode* root) {
    if(root == NULL) {
        return NULL;
    }
    cout << root -> val << endl;
    Inoder(root -> left);
    Inoder(root -> right);
}
```

## Postorder Traversal

```cpp
void Inorder(TreeNode* root) {
    if(root == NULL) {
        return NULL;
    }
    Inoder(root -> left);
    Inoder(root -> right);
    cout << root -> val << endl;
}
```

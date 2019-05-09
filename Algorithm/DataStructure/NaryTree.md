# N-ary Tree

## Types of N-ary Tree

- A **full k-ary tree** is a k-ary tree where within each level every node has either 0 or k children.
- A **perfect k-ary tree** is a full k-ary tree in which all leaf nodes are at the same depth.
- A **complete k-ary tree** is a k-ary tree which is maximally space efficient. It must be completely filled on every level except for the last level. However, if the last level is not complete, then all nodes of the tree must be "as far left as possible".

## Difinition

```cpp
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
```

## Recursive Postorder Traversal

```cpp
vector<int> RecursivePostorder(Node* root) {
    vector<int> res;
    if(!root) {
        return res;
    }
    for(Node* child : root -> children) {
        vector<int> temp;
        temp = IterativelyPostorder(child);
        res.insert(res.end(), temp.begin(), temp.end());
    }
    res.push_back(root -> val);
    return res;
}
```

## Iteratively Postorder Traversal

```cpp
vector<int> IterativelyPostorder(Node* root) {
    vector<int> res;
    vector<Node*> temp{root};
    if(!root){
        return res;
    }
    while(!temp.empty()){
        int n = temp.size();
        for(int i = 0; i < n; i++){
            Node *cur = temp.back();
            temp.pop_back();
            temp.insert(temp.end(), cur -> children.begin(), cur -> children.end());
            res.insert(res.begin(), cur -> val);
        }
    }
    return res;
}
```

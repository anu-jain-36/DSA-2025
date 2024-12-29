#include <iostream>
using namespace std;
struct Node{
    int key;
    Node* left;
    Node* right; 
    Node(int item)
    {
        key=item;
        left= nullptr;
        right= nullptr;
    }
};

Node* insert(Node* node,int item)
{
    if(node == nullptr)
        {
        // cout<<"I am here creating root node";
        return new Node(item);
        }
    else if (node->key== item)
        return node;
    else if(node->key < item)
            {
            // cout <<"key is "<<item;
            // cout<<"inserting in the right subtree";
            node->right= insert(node->right, item);
            }
    else 
    {
            // cout <<"key is "<<item;
            // cout<<"inserting in the left subtree";
            node->left = insert(node->left, item);
            }
    return node;
}

void inorder(Node* root)
{
    if (root != nullptr)
    {
          inorder(root->left);
          cout<<root->key<<" ";
          inorder(root->right);
    }
  
}

int main()
{
    Node* root = new Node(10);
    root= insert(root, 20);
    root=insert (root, 7);
    root= insert (root,3);
    root= insert (root,30);
    root= insert (root,50);
    root= insert (root,8);
    root= insert (root,40);
    inorder(root);
    return 0;
}
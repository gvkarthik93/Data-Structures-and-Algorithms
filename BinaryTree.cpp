#include<iostream>
using namespace std;

// Binary tree works on O (logN) for insert/search/delete operations.

// PreOrder - Parent, Left, Right
// PostOrder - Left, Right, Parent
// Inorder - Left, Parent, Right
// LevelOrder - Binary Tree order (i, 2i+1, 2i+2)

struct node {
	int data;
	node *left;
	node *right;
}*root;

// Function to create a new Node in heap
node* GetNewNode(int data) {
	node* newNode = new node();
	newNode->data = data;
	newNode->left = newNode->right = NULL;
	return newNode;
}

// To insert data in BST, returns address of root node 
node* Insert(node* root,int data) {
	if(root == NULL) { // empty tree
		root = GetNewNode(data);
	}
	// if data to be inserted is lesser, insert in left subtree. 
	else if(data < root->data) {
		root->left = Insert(root->left,data);
	}
	// else, insert in right subtree. 
	else {
		root->right = Insert(root->right,data);
	}
	return root;
}

//To search an element in BST, returns true if element is found
bool Search(node* root,int data) {
	if(root == NULL) {
		return false;
	}
	else if(root->data == data) {
		return true;
	}
	else if(data <= root->data) {
		return Search(root->left,data);
	}
	else {
		return Search(root->right,data);
	}
}

int main() {
	root = NULL;

	/*Code to test the logic*/
	root = Insert(root,15);	
	root = Insert(root,10);	
	root = Insert(root,20);
	root = Insert(root,25);
	root = Insert(root,8);
	root = Insert(root,12);

	// Ask user to enter a number.  
	int number;
	cout<<"Enter number be searched\n";
	cin>>number;
	//If number is found, print "FOUND"
	if(Search(root,number) == true) cout<<"Found\n";
	else cout<<"Not Found\n";
}
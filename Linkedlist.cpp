#include<iostream>
using namespace std;

struct node {
	int data;
	node* next;
};

int listLength (node* head);

int main() {
	return 0;
}

// Calculating the length of the linked list
int listLength (node* head) {
	node* current = head;
	int count = 0;
	while (current != NULL) {
		count++;
		current = current->next;
	}
}

// Insert a node at any given position
void insertNode(node* head, int newdata, int position) {
	int k = 1;
	node *p, *q, *newnode;
	
	newnode = (node *)malloc(sizeof(node));
	if (!newnode) {
		cout<<"Memory Error: Unable to create memory for new node"<<endl;
		return;
	}

	newnode->data = newdata;
	p = head;

	if (position == 1) {
		newnode->next = p;
		head = newnode;
	}
	else {
		while (p!=NULL && k<position) {
			k++;
			q = p;
			p = p->next;
		}
		q->next = newnode;
		newnode->next = p;
	}
}
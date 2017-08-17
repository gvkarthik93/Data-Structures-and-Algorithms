#include<iostream>
using namespace std;

struct node {
	int data;
	node* next;
} *start;

int listLength();
void create(int data);
void insertNode(int newdata, int position);
void updateNode(int newdata, int position);
void deleteNode(int position);
void displayList();

int main() {
	int choice;
	int newdata, position;

	start = NULL;

	do {
		cout<<endl<<"1. Create"<<endl<<"2. Insert"<<endl<<"3. Update"<<endl<<"4. Delete"<<endl<<"5. Display"<<endl<<"6. List Length"<<endl<<"7. Exit"<<endl;
		cout<<"Enter your option: ";
		cin>>choice;
		switch (choice) {
			case 1: cout<<"Enter data: ";
					cin>>newdata;
					create(newdata);
					displayList();
					break;
			case 2: cout<<"Enter data: ";
					cin>>newdata;
					cout<<"Enter position: ";
					cin>>position;
					insertNode(newdata, position);
					displayList();
					break;
			case 3: cout<<"Enter data: ";
					cin>>newdata;
					cout<<"Enter position of Node to be updated: ";
					cin>>position;
					updateNode(newdata, position);
					displayList();
					break;
			case 4: cout<<"Enter position of node to be deleted: ";
					cin>>position;
					deleteNode(position);
					displayList();
					break;
			case 5: displayList();
					break;
			case 6: listLength();
					break;
			case 7: break;
			default: displayList();
					break;
		}
	} while (choice != 7);
	return 0;
}

// Calculating the length of the linked list
int listLength() {
	node* current = start;
	int count = 0;
	while (current != NULL) {
		count++;
		current = current->next;
	}
	cout<<endl<<"List Length: "<<count<<endl;
	return count;
}

// Creating a new linked list. you could also create a linked list by using inset at position 1
void create(int newdata) {
	node* temp;
	temp = (node *)malloc(sizeof(node));
	if (start == NULL) {
		temp->data = newdata;
		temp->next = NULL;
		start = temp;
	}
}

// Insert a node at any given position
void insertNode(int newdata, int position) {
	int k = 1;
	node *p, *q, *newnode;
	
	newnode = (node *)malloc(sizeof(node));
	if (!newnode) {
		cout<<"Memory Error: Unable to create memory for new node"<<endl;
		return;
	}

	newnode->data = newdata;
	p = start;

	if (position == 1) {
		newnode->next = p;
		start = newnode;
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

// Code block to update node at a specific posiiton
void updateNode(int newdata, int position) {
	int k = 0;
	node *p, *q;
	p = start;
	if (position > listLength()) {
		cout<<endl<<"Node doesn't exist"<<endl;
	}
	else {
		while (k != position) {
			k++;
			q = p;
			p = p->next;
		}
		q->data = newdata;
	}
}

// COde block for deleting a node at a specific position
void deleteNode(int position) {
	int k = 1;
	node *p, *q;
	if (start == NULL) {
		cout<<endl<<"List is Empty"<<endl;
		return;
	}

	p = start;
	if (position == 1) {
		start = start->next;
		free(p);
		return;
	}
	else {
		while (p != NULL && k < position) {
			k++;
			q = p;
			p = p->next;
		}
		if (p == NULL) {
			cout<<endl<<"Position does not exist"<<endl;
		}
		else {
			q->next = p->next;
			free(p);
		}
	}
}

// Code block to display the linked list
void displayList() {
	node *p;
	p = start;

	if (p==NULL) {
		cout<<endl<<"List is empty"<<endl;
		return;
	}

	while(p!=NULL) {
		cout<<p->data<<" ";
		p = p->next;
	}
	cout<<endl;
}
#include<iostream>
using namespace std;

struct node {
	int data;
	node* next;
} *start;

int listLength (node* head);
void create(int data);
void insertNode(int newdata, int position);
void updateNode(node* head, int newdata, int position);
void deleteNode(node* head, int newdata, int position);
void displayList();

int main() {
	int choice;
	int newdata, position;

	start = NULL;

	do {
		cout<<endl<<"1. Create"<<endl<<"2. Insert"<<endl<<"3. Update"<<endl<<"4. Delete"<<endl<<"5. Display"<<endl<<"6. Exit"<<endl;
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
					//updateNode(head, newdata, position);
					displayList();
					break;
			case 4: cout<<"Enter position of node to be deleted: ";
					cin>>position;
					//deleteNode(head, newdata, position);
					displayList();
					break;
			case 5: displayList();
					break;
			case 6: break;
			default: displayList();
					break;
		}
	} while (choice != 6);
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
	return count;
}

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

void updateNode(node* head, int newdata, int position) {
}

void deleteNode(node* head, int newdata, int position) {
}

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
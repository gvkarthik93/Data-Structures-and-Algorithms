#include<iostream>
using namespace std;

bool isEmpty();
void push(int);
void pop();
void displayList();

struct node {
	int data;
	node *next;
}*start, *tail;

int main() {
	int choice;

	do {
		cout<<endl<<"1. Push"<<endl<<"2. Pop"<<endl<<"3. Display"<<endl<<"4. Exit"<<endl;
		cout<<"Enter choice: ";
		cin>>choice;
		switch(choice) {
			case 1: int newData;
					cout<<endl<<"Enter data to be pushed: ";
					cin>>newData;
					push(newData);
					break;
			case 2: pop();
					break;
			case 3: displayList();
					break;
			case 4: break;
			default: cout<<endl<<"Incorrect choice"<<endl;
					break;
		}
	} while(choice != 4);
}

bool isEmpty() {
	node *p;
	p = start;
	if (p==NULL) {
		return true;
	}
	else {
		return false;
	}
}

void push(int newData){
	node *p, *q;
	p = (node *)malloc(sizeof(node));
	if (start == NULL) {
		p->data = newData;
		p->next = NULL;
		start = p;
		tail = p;
	}
	else {
		p->data = newData;
		p->next = NULL;
		tail->next = p;
		tail = p;
	}

	displayList();
}

void pop() {
	node *p, *q;
	p = start;
	if (isEmpty()) {
		cout<<endl<<"Stack is Empty"<<endl;
		return;
	}
	else {
			q = p->next;
			start = q;
			free(p);
			displayList();
		}
}

void displayList() {
	node *p;
	p = start;

	if (isEmpty()) {
		cout<<endl<<"Stack is empty"<<endl;
		return;
	}

	while(p!=NULL) {
		cout<<p->data<<" ";
		p = p->next;
	}
	cout<<endl;
}
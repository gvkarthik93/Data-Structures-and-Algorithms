#include<iostream>
using namespace std;

void linearSearch();
int main() {
	linearSearch();
}

// Linear Search
// Time complexity is O(n)
void linearSearch() {
	int arr[10] = {11,3,2,4,112,34,23,43,55,22};
	int i, num;
	cout<<endl<<"Enter element to be searched: ";
	cin>>num;
	for(i=0;i<10;i++) {
		if (arr[i] == num) {
			cout<<endl<<"Element Found"<<endl;
			break;
		}
	}
}

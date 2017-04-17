#include<iostream>
using namespace std;

void bubbleSort();
void modifiedBubbleSort();
void selectionSort();

int main() {
    bubbleSort();
    cout<<endl;
    modifiedBubbleSort();
    cout<<endl;
    selectionSort();
    cout<<endl;
    return 0;
}

void bubbleSort() {
    int arr[5] = {2,5,1,4,3};
    int n = sizeof(arr)/sizeof(arr[0]);

    for(int i=0;i<n;i++)
    {
        for (int j=0;j<n-1;j++)
        {
            if (arr[j]>arr[j+1])
            {
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
        }
    }

    for (int k=0;k<n;k++)
    {
        cout<<arr[k]<<" ";
    }
}

void modifiedBubbleSort() {
    int arr[5] = {2,5,1,4,3};
    int n = sizeof(arr)/sizeof(arr[0]);
    int flag = 0;
    for(int i=0;i<n;i++)
    {
        for (int j=0;j<n-1;j++)
        {
            if (arr[j]>arr[j+1])
            {
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                flag = 1;
            }
        }
        if (flag == 0)
            break;
    }

    for (int k=0;k<n;k++)
    {
        cout<<arr[k]<<" ";
    }
}

void selectionSort() {
    int arr[5] = {2,5,1,4,3};
    int n = sizeof(arr)/sizeof(arr[0]);

    for (int i=0; i<n-1; i++)
    {
        int min_index = i;
        for (int j=i+1; j<n;j++)
        {
            if (arr[min_index] > arr[j])
            {
                min_index = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }

    for (int k=0;k<n;k++)
    {
        cout<<arr[k]<<" ";
    }
}

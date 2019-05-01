#include <iostream>
#include <vector>
using namespace std;

void InsertionSort(vector<int>& array){
    for(int i = 1; i < array.size(); i++){
        int key = array[i];
        int j = i - 1;
        while(j >= 0 && key < array[j]){
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = key;

        cout << "step " << i << ": ";
        for(int i = 0; i < array.size(); i++){
            cout << array[i] << " ";
        }
        cout << endl;
    }
}

int main(){
    vector<int> array = {1, 9, 2, 8, 6, 5, 7, 4};
    InsertionSort(array);
    for(int i = 0; i < array.size(); i++){
        cout << array[i] << " ";
    }
    return 0;
}
#include <iostream>
#include <vector>
using namespace std;

void Merge(vector<int>& array, vector<int>& left, vector<int>& right){
    int length1 = left.size();
    int length2 = right.size();

    int i = 0, j = 0;

    while(i < length1 || j < length2){
        if(i >= length1){
            array.push_back(right[j++]);
        }else if(j >= length2){
            array.push_back(left[i++]);
        }else if(left[i] < right[j]){
            array.push_back(left[i++]);
        }else{
            array.push_back(right[j++]);
        }
    }
}

void MergeSort(vector<int>& array){
   int length = array.size();
   if(length <= 1){
       return;
   }
   vector<int> left;
   vector<int> right;

   for(int i = 0; i < length; i++){
       if(i < length / 2){
           left.push_back(array[i]);
       }else{
           right.push_back(array[i]);
       }
   }

   MergeSort(left);
   MergeSort(right);
   array.clear();
   Merge(array, left, right);
}

int main(){
    vector<int> array = {1, 5, 3, 7, 4, 9, 2, 13, 10};
    MergeSort(array);
    for(int i = 0; i < array.size(); i++){
        cout << array[i] << " ";
    }
    return 0;
}
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    string s = "babad";
    string s_new = "";
    s_new += '$';
    s_new += '#';
    for (int i = 0; i < s.size(); i++)
    {
        s_new += s[i];
        s_new += '#';
    }
    s_new += '&'; 
    cout << s_new << endl;

    vector<int> p(s_new.size(), 0);
    int max = 0;
    int mx = 0;
    int id = 0;
    int center = 0;
        
    for(int i = 0; i < s_new.size(); ++i){
        if(i < mx){
            p[i] = min(p[2*id - i], mx - i);
        }else{
            p[i] = 1;
        }
        while(s_new[i - p[i]] == s_new[i + p[i]]){
            p[i]++;
        }
        if(i + p[i] > mx){
            id = i;
            mx = i + p[i];
        }
 
        if(p[i] > max){
            max = p[i];
            center = i;
        }
    }
    string result;
    for(int i = center - max + 1; i < center + max - 1; ++i){
        if(s_new[i] != '#')
        result += s_new[i];
    }
    cout << result << endl;
    return 0;
}
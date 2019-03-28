#include <bits/stdc++.h>
using namespace std;

bool isChar(char ch){
    if(ch>='a' and ch<='z') return 1;
    if(ch>='A' and ch<='Z') return 1;
    return 0;
}

set<string> S;

void ins(string& s){
    string tmp;
    for(auto x: s){
        if(!isChar(x) and !(x=='\'')) return;
        tmp+=tolower(x);
    }
    S.insert(tmp);
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    string s;
    while(cin>>s){
        ins(s);
    }
    for(auto &x: S){
        printf("%s\n", x.c_str());
    }

    return 0;
}
#include<iostream>
using namespace std;

int main(){
    int a,b;
    cout<<"enter the first number (a):"<<endl;
    cin>>a;
    cout<<"enter the second number(b):"<<endl;
    cin>>b;
    a=a-b;
    b=a+b;
    a=b-a;
    cout<<"After swapping new first number(a):"<<a<<endl;
    cout<<"After swapping new second number(b):"<<b<<endl;
    return 0;
}
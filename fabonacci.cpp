#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter the number of terms required in series:";
    cin>>n;
    int term=0,a=0,b=1;
    cout<<"the fabonacci series is:"<<endl;
    cout<<a<<","<<b<<",";
    for(int i=1;i<=n;i++){
        term=a+b;
        cout<<term<<",";
        
        a=b;
        b=term;
    }
    cout<<endl;
    return 0;
}
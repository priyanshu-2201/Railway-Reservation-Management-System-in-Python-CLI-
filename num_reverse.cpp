#include<iostream>
using namespace std;

int reverse(int k){
    int rev=0;
    k=k*10;
    while (k>0){
        int x=0;
        x=k%10;
        k=k/10;
        rev=rev*10+x;
    }
}
int main(){
    int a;
    cout<<"enter the number:";
    cin>>a;
    int n;
    n=reverse(a);

    cout<<"reverse of the given number:"<<n;
    return 0;
}
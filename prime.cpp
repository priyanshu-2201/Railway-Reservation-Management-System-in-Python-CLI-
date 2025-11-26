#include<iostream>
using namespace std;

int main(){
    int a;
    int x=0;
    cout<<"Enter the number:";
    cin>>a;
    for (int n=2;n<a;n++){
        if (a%n==0){
            cout<<"The given number is not a prime number"<<endl;
            cout<<"The given number is divisible by:"<<n<<endl;
            x=1;
            break;
        }
    }

    if (x==0){
        cout<<"The given number is a prime number"<<endl;

    }
    return 0;
}
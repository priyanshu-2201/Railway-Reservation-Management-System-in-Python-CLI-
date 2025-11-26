#include<iostream>
using namespace std;

int factorial (int n){
        int fact=n;
        for(fact>1;fact-=1;){
            n=n*fact;
        
        }

        return n;
}

int main(){ 
    int a;
    int k;
    cout<<"enter the number whose factorial is to be calculated:";
    cin>>k;
    a=factorial(k);
    cout<<"the factorial of the given number is:"<<a;

}
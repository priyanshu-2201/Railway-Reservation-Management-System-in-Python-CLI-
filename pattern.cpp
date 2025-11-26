#include<iostream>
using namespace std;
 int main(){
    int n=5;
    for(int i=0;i<=n;i++){

        for(int j=n;j>=i;j-=1){
            
            cout<<" ";
        }

        cout<<"*";
        for(int m=1;m<=i;m++){
            
            cout<<" ";

        }

        for(int m=1;m<=i;m++){
            
            cout<<" ";

        }

        cout<<"*";

        cout<<endl;

    }

    for(int i=0;i<=n;i++){
        for(int m=1;m<=i;m++){
            
            cout<<" ";
        }
        cout<<"*";
        for(int j=n;j>=i;j-=1){
            
            cout<<" ";
        }
        for(int j=n-1;j>=i;j-=1){
            
            cout<<" ";
        }
        cout<<"*\n";

    }
    cout<<endl;
    return 0;
 }
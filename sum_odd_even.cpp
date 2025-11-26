#include<iostream>
using namespace std;

int main(){
   int sum_odd=0,sum_eve=0;
   int m;
   cout<<"enter the upper limit:";
   cin>>m;
   for(int n=0;n<=m;n++){
      if (n%2==0){
         sum_eve=sum_eve+n;

      } else{
         sum_odd=sum_odd+n;
      }
    }
    cout<<endl;
    cout<<"sum of odd numbers:"<<sum_odd<<endl;
    cout<<"sum of even numbers:"<<sum_eve<<endl;
    return 0;

}
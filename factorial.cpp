#include <iostream>
using namespace std;
int main(){

    int a;
    cout<<"enter the number whose factorial is to be calculated:"<<endl;
    cin>>a;
    int f=a;
    for (a>1; a-=1;){
        f*=a;
    }
    cout<<"the factorial of the given number is:"<<f<<endl;
    return 0;
}

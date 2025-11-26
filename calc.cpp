#include <iostream>
using namespace std;
int main() {
    
    cout<<"Welcome to calculator\n"<<"1. Addition"<<endl;
    cout<<"2. Subtraction"<<endl;
    cout<<"3. Multiplication"<<endl;
    cout<<"4. Division"<<endl;
    
    int s;
    cout<<"Enter your choice:"<<endl;
    cin>>s;
    int a,b;
    cout<<"input the first number:"<<endl;
    cin>>a;
    
    cout<<"input the second number:"<<endl;
    cin>>b;
    
    if (s==1){

        int sum=a+b;

        cout<<"the sum of both numbers:"<<sum<<endl;

    }else if (s==2){

        int subtract=a-b;
        cout<<"the difference of both numbers:"<<subtract<<endl;
    }else if (s==3){

        double multiply=a*b;
        cout<<"the product of both numbers:"<<multiply<<endl;

    }else if (s==4){

        double division=a/b;
        cout<<"the result of division of both numbers:"<<division<<endl;

    }else{

        cout<<"please enter a valid choice (1-4)"<<endl;

    }
    return 0;

}
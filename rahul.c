#include<stdio.h>

int main(){
int a=0,b=1,z,n;

printf("enter the number of digit you want in the fibonacci:");
scanf("%d",&n);
for(int i=1;i<=n;i++){
    printf("%d\n",a);
    z=a+b;
    a=b;
    b=z;

}
return 0;
}

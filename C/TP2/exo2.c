#include <stdio.h>

void table(int);

int main(){
    int a;
    printf("entrez un nombre : ");
    scanf("%d", &a);
    table(a);
}

void table(int a){
    for(int i =0;i<11;i++){
        int b;
        b=a*i;
        printf("%d x %d = %d\n",a,i,b);
    }
}
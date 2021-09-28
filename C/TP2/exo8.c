#include <stdio.h>

int main(){
    float r;
    int a;
    r=0;
    printf("entrez un nombre : ");
    scanf("%d", &a);
    r= (4/3)*3.14*(a*a*a);
    printf("V = %f\n",r);
}
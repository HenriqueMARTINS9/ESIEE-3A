#include <stdio.h>
int main () {
    int a,b;
    char* c;
    printf("\n entrez un nombre : ");
    scanf("%d" , &a);
    b = a%2;
    c = b == 0 ? "nombre pair " : "nombre impair ";
    printf(" %d est un %s\n",a,c);
    return 0;
}
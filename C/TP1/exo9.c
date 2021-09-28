#include <stdio.h>
int main() {
    int a,b;
    printf("entrez une valeur (1/2) :");
    scanf("%d", &a);
    printf("entrez une valeur (2/2) :");
    scanf("%d", &b);
    a  =  b-a;
    b  =  b-a;
    a  =  a+b;
    printf("%d %d\n",a,b);
    return 0;
}

/* ce programme inverse deux valeures avec uniquement 2 variables */ 
#include <stdio.h>
int main () {
    int a;
    printf("entrez une valeur = ");
    scanf("%d", &a);
    a = 2*a;
    printf("le double de la valeur est %d\n",a);
    return 0;
}
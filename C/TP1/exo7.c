#include <stdio.h>
int main () {
    int a;
    float b;
    printf("entrez une valeur = ");
    scanf("%d", &a);
    b = 1.20*a;
    printf("prix HT = %d\nprix TTC %f\n",a,b);
    return 0;
}
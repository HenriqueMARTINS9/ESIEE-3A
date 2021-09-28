#include <stdio.h>
int main () {
    int a,b,c;
    printf("entrez une valeur (1/2) a = ");
    scanf("%d", &a);
    printf("entrez une valeur (2/2) b = ");
    scanf("%d", &b);
    c=a;
    a=b;
    b=c;
    printf("\n desormais:\na = %d\nb = %d\n", a,b);
    return 0;
}
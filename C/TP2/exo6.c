#include <stdio.h>
int main () {
    int a,b,c,d;
    printf("entrez un nombre (1/3) : \n");
    scanf("%d", &a);
    printf("entrez un nombre (2/3) : \n");
    scanf("%d" ,&b);
    printf("entrez un nombre (3/3) : \n");
    scanf("%d" ,&c);
    d = a-b <= 0 ? (b-c<0 ? c : b) : a;
    printf("le nombre maximum est %d\n", d);
    return 0;
}
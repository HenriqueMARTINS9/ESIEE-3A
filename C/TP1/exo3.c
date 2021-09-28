#include <stdio.h>
int main () {
    int a,b;
    printf("entrez un nombre : \n");
    scanf("%d", &a);
    printf("entrez un nombre : \n");
    scanf("%d" ,&b);
    if(a>b) {
        printf("le plus grand nombre est %d\n" ,a);
    }
    if(a<b){
        printf("le plus grand nombre est %d\n" ,b);
    }
    if(a==b){
        printf("ces nombres sont egaux\n");
    }
    return 0;
}
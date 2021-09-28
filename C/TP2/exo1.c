#include <stdio.h>

int main () {
    int l,L,S;
    printf("entrez la longueur : ");
    scanf("%d" ,&l);
    printf("entrez la largeur : ");
    scanf("%d" ,&L);
    S = l*L;
    printf("surface = %d m^2\n", S);
}
#include <stdio.h>
int main() {
    int a,b,c;
    printf("entrez une valeur (1/3) :");
    scanf("%d", &a);
    printf("entrez une valeur (2/3) :");
    scanf("%d", &b);
    printf("entrez une valeur (3/3) :");
    scanf("%d", &c);
    a  =  a + b + c ;
    b  =  b +c ;
    c  =  a -c ;
    a  =  a -c ;
    b  =  c -b + a;
    c  =  c -b;
    printf("%d %d %d\n",a,b,c);
    return 0;
}
 /* ce programme inverse l'ordre des trois variables : 
 a=>c b=>c c=>a */
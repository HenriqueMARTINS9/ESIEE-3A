#include <stdio.h>
int main () {
    int a,b,c;
    printf("\nentrez un nombre : ");
    scanf("%d",&a);
    printf("\nentrez un autre nombre : ");
    scanf("%d",&b);
    c = a-b;
    int r = c > 0 ? c :-c ;
  printf("*val abs est egalee :%d\n",r);
}

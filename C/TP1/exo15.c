#include <stdio.h>

int main () {
    int n,i,r;
    printf("entrez un nombre : ");
    scanf("%d", &n);
    r=n;
    for(i=1;i<n;i++){
        printf("i = %d  r= %d \n",i,r);
        r=r*i;
    }
    printf("%d\n",r);
    return 0 ;
}
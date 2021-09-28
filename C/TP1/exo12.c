#include <stdio.h>
int main () {
    int i,n,s;
    printf("entrez n");
    scanf("%d",&n);
    for(i=0;i<n+1;i++){
        s = s+i;        
    }
    printf("%d\n", s);
    return 0;
}
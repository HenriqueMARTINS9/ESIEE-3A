#include <stdio.h>
int main () {
    int i,x,n,b;
    printf("entrez X");
    scanf("%d",&x);
    printf("entrez n");
    scanf("%d",&n);
    if (n == 0){
            b=1;
        }
    else{
        for(i=0;i<n-1;i++){
            if (b <x*x){
                b=x*x;
            }
            else{
                b=b*x;
            }
        }
    }
    printf("%d\n", b);
    return 0;
}
#include <stdio.h>
int main () {
    int i;
    for(i=0;i<11;i++){
        int a;
        a = 9*i;
        printf("%d x 9 = %d\n",i,a);
    }
    return 0;
}
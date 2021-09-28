#include <stdio.h>

float main(){
    float r;
    int a;
    r=0;
    printf("entrez un nombre : ");
    scanf("%d", &a);
    if(a<=10){
        r=r+a*0.5;
    }
    if(a<=30 && a>10){
        r=r+5+(a-10)*0.3;
    }
    if(a>=30){
        r=r+5+6+(a-30)*0.20;
    }
    printf("prix final = %.2f \n", r);
}
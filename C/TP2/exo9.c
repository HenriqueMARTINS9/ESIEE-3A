#include <stdio.h>
#include <math.h>

void calcul(float a, float b , float c){
    float d = (powf(b,2))-4*a*c;
    if(d>0){
        float x1 = (-b-sqrtf(d))/(2*a);
        float x2 = (-b+sqrtf(d))/(2*a);
        printf("x1 = %.2f   x2= %.2f\n",x1,x2);
    }
    if(d==0){
        float x1 = -b/(2*a);
        printf("x0 = %.2f\n",x1);
    }
    if(d<0){
        float xr = (-b/2*a);
        float x1i = (-sqrtf(-d))/(2*a);
        float x2i = (+sqrtf(-d))/(2*a);
        printf("x1 = %.2f+i%.2f   x2= %.2f+i%.2f\n",xr,x1i,xr,x2i);
    }
}

int main(){
    float a,b,c;
    printf("entrez a : ");
    scanf("%f", &a);
    printf("entrez b : ");
    scanf("%f", &b);
    printf("entrez c : ");
    scanf("%f", &c);
    calcul(a,b,c);

}
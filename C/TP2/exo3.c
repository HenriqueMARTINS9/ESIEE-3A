#include <stdio.h>
#include <math.h>
#define PI 3.142857
int main (){
    float r,p,a;
    printf("entrez le rayon du cercle : ");
    scanf("%f", &r);
    p = 2*PI*r;
    a = 2*PI*pow(r,2);
    printf("pour un cercle de rayon %f :\nperimètre = %f\naire = %f",r,p,a);
    return 0;
}
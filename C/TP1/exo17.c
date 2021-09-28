#include <stdio.h>
#include <math.h>

double power (int x , int n){
    double m,i;
    m=1;
    for (i=0;i<n;i++){
        m=m*x;
    }
    return m;
}

double factoriel(int n) {
    double i,r;
    r=n;
    for(i=1;i<n;i++){
        r=r*i;
    }
    return r ;
}

double calcul (int x, int p){
    return (power(-1,p))*(power(x,(2*p+1))/factoriel((2*p+1)));
}

long double absolute (long double x){
    if (x<0) {
        return x*(-1);
    }
    else{return x;}
}

long double finalCalcul(int x, int p){
    long double r;
    r=x;
    int i;
    for(i=3;i<=p;i=i+2){
        r=r+calcul(x,p);
    }
    r=r+power(x,(2*p+2));
    return r;
}

int main(){
    int x,p;
    long double e,r;
    r=10;
    printf("entrez un nombre : ");
    scanf("%d",&x);
    printf("entrez un epsilon : ");
    scanf("%Lf",&e);
    p=3;
    while(absolute(r)>e){
        r =calcul(x,p);
        p = p +2;
        printf("p = %d  r = %.40Lf \n",p,r);
    }
    r = finalCalcul(x,p);
    printf("resultat final = %.20Lf\n",r);
    return 0;
}
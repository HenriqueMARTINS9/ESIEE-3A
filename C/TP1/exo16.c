#include <stdio.h>
int calcul(int);

int main(){
    int n,r;
    printf("entrez un nombre : ");
    scanf("%d",&n);
    r = calcul(n);
    printf("resultat = %p \n", &r);
}

int calcul(int x){
    if(x==0){return 1;}
    else{
      return 2*calcul(x-1)+1;
    }
}
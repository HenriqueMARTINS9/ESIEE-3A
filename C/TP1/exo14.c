#include <stdio.h>
#include <stdbool.h>

int main () {
    int a,i;
    bool b;
    b = true;
    printf("entrez un nombre");
    scanf("%i",&a);
    for (i=2;i<a;i++){
        if (a%i == 0){
            b = false;
        }
    }
    if(b==true){
        printf("%i est un nombre premier \n",a);
    }
    else{
        printf("%i n'est pas un nombre premier \n",a);
    }

}


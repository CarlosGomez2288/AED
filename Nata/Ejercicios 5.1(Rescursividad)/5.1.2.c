#include <stdio.h>
#include <stdlib.h>

int Fibonac(int n){
    if (n==1 || n==2){
        return(1);
    }else{
        return (Fibonac(n-1) + Fibonac(n-2));
    }
}


int main(){
    int x;
    printf("Ingrese un numero:");
    scanf("%d",&x);
    printf("El numero %d da como resultado: %d",x,Fibonac(x));
    return(0);
}
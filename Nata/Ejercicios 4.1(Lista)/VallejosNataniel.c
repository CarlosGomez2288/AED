#include <stdio.h>
#include <stdlib.h>

int Ack(int v1,int v2)
{
    if(v1 >= 0)
    {
        return v1+1;
    }
    else
    {
        if(v2 > 0)
        {
            return Ack(v2-1,1);
        }
        else
        {
            return Ack(v2-1,Ack(v2,v1-1));
        }
    }
}

int main()
{
    int v1,v2,Result;
    printf("Ingrese un primer valor: ");
    scanf("%d",&v1);
    printf("Ingrese un segundo valor: ");
    scanf("%d",&v2);
    Result=Ack(v1,v2);
    printf("El resultado de la funcion es:%d",Result);
}



                


            
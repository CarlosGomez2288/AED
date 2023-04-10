
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) {
        Scanner dat = new Scanner(System.in);
        int a;
        int c;
        
        for (int i= 0 ;i<2  ;i++ ){
            System.out.println("Valor: "+ i);
            a = dat.nextInt();
            c= minimo(a);
        } 
        System.out.println(c);
    }
    public static int minimo(int b){
        int aux;
        aux= b;
        if (aux <= b ){
            aux= b;
        }
        return aux;
    }
}

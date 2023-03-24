package TallerProgra_S0;

import java.util.Scanner;

public class Test {

    public static void main(String[] args) {
        /*
        String miTexto = "Texto de variable";
        imprimeTexto("Este es mi Texto");
        imprimeTexto(miTexto);
        imprimeTexto(pideTexto());
*/
        int numeroPedido = pideNumero();

        int numeroCalculado = calculaNumero(numeroPedido);

        imprimeNumero(numeroCalculado);
    }

    static int pideNumero(){
        
        Scanner entrada = new Scanner(System.in);
        int miNumeroEntrada = entrada.nextInt();
        return miNumeroEntrada;
    }

    static int calculaNumero(int sumando){
        int numeroFinal = 0;

        numeroFinal = (int)((Math.random()*10) + 1);
        numeroFinal += sumando;

        return numeroFinal;
    }

    static void imprimeNumero(int texto){
        System.out.println(texto);
    }




    static void imprimeTexto(String texto){
        System.out.println(texto);
    }

    static String pideTexto(){
        
        Scanner entrada = new Scanner(System.in);
        String miEntrada = entrada.nextLine();
        return miEntrada;
    }
}


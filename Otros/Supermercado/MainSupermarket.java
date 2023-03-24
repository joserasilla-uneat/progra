package Supermercado;

import java.util.Scanner;

public class MainSupermarket {
    // System
    public static Scanner userInput = new Scanner(System.in);
    // Constants
    public static int MAX_CASHIERS = 10;
    public static int MIN_CASHIERS = 0;

    public static void main(String[] args) {
        int cashiersAmount = cashierOpening();
        Cashier[] cashiersArray = createCashiers(cashiersAmount);
    }


    public static void Print(String printedText) {
        System.out.println(printedText);
    }

    public static int cashierOpening() {
        Print("¿Cuantas cajas desea abrir?");
        int aux;
        do {
            aux = userInput.nextInt();
            if (aux <= MIN_CASHIERS || aux > MAX_CASHIERS) {
                Print(Texts.errorAmount(MIN_CASHIERS, MAX_CASHIERS));
            }
        } while (aux <= 0 || aux > 10);
        return aux;
    }

    public static Cashier[] createCashiers(int amount){
        Cashier[] cashiers = new Cashier[amount];
        for(int i = 0; i+1 >= amount; i++){
            cashiers[i] = new Cashier("Caja" + i);
        }
        return cashiers;
    }

}
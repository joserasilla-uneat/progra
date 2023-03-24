package Supermercado;

public class Client {
    
    public int itemsAmount;
    public Cashier myCashier;

    public Client (int items, Cashier cashier) {
        itemsAmount = items;
        myCashier = cashier;
    }

}

public class Vehicle {

    // VARIABLES
    int wheels;
    int doors;
    boolean turnedOn = false;
    String brand;
    String model;

    public Vehicle(int wheels, int doors, String brand, String model){
        this.wheels = wheels;
        this.doors = doors;
        this.brand = brand;
        this.model = model;
    }


    public String getBrand(){
        return brand;
    }

    public void setBrand(String brand){
        this.brand = brand;
    }

    public int getWheels() {
        return wheels;
    }

    public void setWheels(int wheels) {
        this.wheels = wheels;
    }

    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }

    public boolean getTurnedOn() {
        return turnedOn;
    }

    public void setTurnedOn(boolean turnedOn) {
        this.turnedOn = turnedOn;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }


    public void Move(){
        while(getTurnedOn()){
            System.out.println("I'm moving!");
        }
        if (!getTurnedOn()){
            System.out.println("Vehicle isn´t on");
        }
    }

    public void StartEngine(){
        setTurnedOn(true);
    }

    public void TurnOff(){
        setTurnedOn(false);
    }

}

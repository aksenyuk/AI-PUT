import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;
import java.util.logging.Level;
import java.util.logging.Logger;


public class Comodity extends Asset{

    private double exchangeRate;

    public double getExchangeRate(){
        return exchangeRate;
    }
    public void setExchangeRate(float exchangeRate){
        this.exchangeRate = exchangeRate;
    }

    ArrayList<Double> listOfComodityPrices = new ArrayList();

    public ArrayList<Double> getListOfComodityPrices(){
        return listOfComodityPrices;
    }

    public void addToListComodityOfPrices(double price){
        listOfComodityPrices.add(price);
    }

    public void run(){
        while(true){
                setCurrentPrice(this.getCurrentPrice() + (float)(Math.random() * (10 - 1)) + 1);
        }
    }

}

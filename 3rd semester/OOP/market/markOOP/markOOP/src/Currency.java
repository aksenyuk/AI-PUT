import java.util.*;

public class Currency extends Asset{
    private String nameOfCurrency;
    private float exchangeRate;

    Collection<String> listOfLegalCountries = new ArrayList();
    public String getNameOfCurrency(){ return nameOfCurrency;}
    public float getExchangeRate(){
        return exchangeRate;
    }

    public void addToListOfLegalCountries(String country){
        listOfLegalCountries.add(country);
    }

    public void setExchangeRate(float exchangeRate){
        this.exchangeRate = exchangeRate;
    }

    ArrayList<Double> listOfCurrencyPrices = new ArrayList();

    public ArrayList<Double> getListOfCurrencyPrices(){
        return listOfCurrencyPrices;
    }

    public void addToListCurrencyOfPrices(double price){
        listOfCurrencyPrices.add(price);
    }
}

import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Company extends Asset implements Runnable{

    private String nameOfCompany;
    private String IPOdate;
    private float IPOshareValue;
    private float openingPrice;
    private float profit;
    private float revenue;
    private float capital;
    private float tradingVolume;
    private float totalSales;

    ArrayList<Double> listOfPrices = new ArrayList();

    public ArrayList<Double> getListOfPrices(){
        return listOfPrices;
    }

    public void addToListOfPrices(double price){
        listOfPrices.add(price);
    }

    public float getOpeningPrice() {
        return openingPrice;
    }

    public float getCapital() {
        return capital;
    }

    public float getProfit() { return profit; }

    public float getRevenue() {
        return revenue;
    }

    public float getTradingVolume() {
        return tradingVolume;
    }

    public float getIPOshareValue() {
        return IPOshareValue;
    }

    public float getTotalSales() { return totalSales; }

    public String getIPOdate() {
        return IPOdate;
    }

    public String getNameOfCompany() {
        return nameOfCompany;
    }

    public void setParametersOfCompany(String nameOfCompany, String IPOdate, int IPOshareValue, float openingPrice, float profit, float revenue, float capital, float tradingVolume, float totalSales) {
        this.capital = capital;
        this.profit = profit;
        this.IPOdate = IPOdate;
        this.revenue = revenue;
        this.nameOfCompany = nameOfCompany;
        this.IPOshareValue = IPOshareValue;
        this.openingPrice = openingPrice;
        this.totalSales = totalSales;
        this.tradingVolume = tradingVolume;
    }

    public void setChanges(float profit, float revenue, float capital, float totalSales, float IPOshareValue) {
        this.capital = capital;
        this.profit = profit;
        this.revenue = revenue;
        this.totalSales = totalSales;
        this.IPOshareValue = IPOshareValue;
    }

    public void increaseNoOfTotalSales() {
        synchronized (this) {
            float percent_max = (float) 0.15 * totalSales;
            float percent_min = (float) 0.5 * totalSales;
            this.totalSales += (int) (Math.random() * ((percent_max - percent_min) + percent_min));
        }
    }

    public void run(){
        while(true){
            this.increaseNoOfTotalSales();
        }
    }
}

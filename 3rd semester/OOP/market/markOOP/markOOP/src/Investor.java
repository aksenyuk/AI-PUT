import java.util.*;

public class Investor {
    private float investmentBudget;

    public float getInvestmentBudget() {
        return investmentBudget;
    }

    public void setInvestmentBudget(float investmentBudget) {
        this.investmentBudget = investmentBudget;
    }

    public void increaseInvestmentBudget() throws InterruptedException{
        synchronized(this){
            this.setInvestmentBudget(this.getInvestmentBudget() + (float)(Math.random() * (1000000 - 100000)) + 100000);
        }
    }

    ArrayList<Comodity> owningsComodity = new ArrayList();
    ArrayList<Currency>owningsCurrency = new ArrayList();
    ArrayList<Company>owningsStocks = new ArrayList();

    ArrayList<Comodity>availableComodities = new ArrayList();
    public void setAvailableComodities(Comodity comodity){
        availableComodities.add(comodity);
    }

    ArrayList<Currency>availableCurrencies = new ArrayList();
    public void setAvailableCurrencies(Currency currency){
        availableCurrencies.add(currency);
    }

    ArrayList<Company>availableStocks = new ArrayList();
    public void setAvailableStocks(Company stock){
        availableStocks.add(stock);
    }

    String nameOfPrInvestor;
    public void setNameOfPrInvestor(String name){
        this.nameOfPrInvestor = name;
    }


    public void buyComodity() throws InterruptedException {
        synchronized (this) {
            if (investmentBudget > 0 && availableComodities.size() != 0) {
                Comodity selectedComodity = availableComodities.get((int)(Math.random() * ((availableComodities.size() - 1) - 0)) + 0);
                if (investmentBudget >= selectedComodity.getExchangeRate()) {
                    investmentBudget = investmentBudget - (float) selectedComodity.getExchangeRate();
                    owningsComodity.add(selectedComodity);
                    float percent_max = (float) 0.8 * selectedComodity.getCurrentPrice();
                    float percent_min = (float) 0.5 * selectedComodity.getCurrentPrice();
                    selectedComodity.setCurrentPrice(selectedComodity.getCurrentPrice() + (float)(Math.random() * (percent_max - percent_min)) + percent_min);
                    System.out.println("Investor " + this.nameOfPrInvestor + " purchased the comodity called: " + selectedComodity.getNameOfUnit());
                    selectedComodity.addToListComodityOfPrices(selectedComodity.getCurrentPrice());
                }
            }
        }
    }


    public void buyCurrency() throws InterruptedException {
        synchronized (this) {
            if (investmentBudget > 0 && availableCurrencies.size() != 0) {
                Currency selectedCurrency = availableCurrencies.get((int)(Math.random() * ((availableCurrencies.size() - 1) - 0)) + 0);
                if (investmentBudget >= selectedCurrency.getExchangeRate()) {
                    investmentBudget = investmentBudget - selectedCurrency.getExchangeRate();
                    owningsCurrency.add(selectedCurrency);
                    selectedCurrency.setExchangeRate(selectedCurrency.getExchangeRate() + (float)(Math.random() * (5 - 1)) + 1);
                    System.out.println("Investor " + this.nameOfPrInvestor + " purchased the currency called: " + selectedCurrency.getNameOfUnit());
                    selectedCurrency.addToListCurrencyOfPrices(selectedCurrency.getExchangeRate());
                }
            }
        }
    }


    public void buyStock() throws InterruptedException {
        synchronized (this) {
            if (investmentBudget > 0 && availableStocks.size() != 0) {
                Company selectedStock = availableStocks.get((int)(Math.random() * ((availableStocks.size() - 1) - 0)) + 0);
                if (investmentBudget >= selectedStock.getIPOshareValue() && selectedStock.getTradingVolume() != 0) {
                    investmentBudget = investmentBudget - selectedStock.getIPOshareValue();
                    owningsStocks.add(selectedStock);
                    float percent_max = (float) 0.3 * selectedStock.getIPOshareValue();
                    float percent_min = (float) 0.1 * selectedStock.getIPOshareValue();
                    selectedStock.setChanges(selectedStock.getProfit() + selectedStock.getIPOshareValue(), selectedStock.getRevenue() + selectedStock.getIPOshareValue(), selectedStock.getCapital() + selectedStock.getIPOshareValue(), selectedStock.getTotalSales() + 1, selectedStock.getIPOshareValue() + (float)(Math.random() * (percent_max - percent_min)) + percent_min);
                    System.out.println("Investor " + this.nameOfPrInvestor + " purchased the stock from the company called: " + selectedStock.getNameOfCompany());
                    selectedStock.addToListOfPrices(selectedStock.getIPOshareValue());
                }
            }
        }
    }

    public void sellComodity() throws InterruptedException {
        synchronized (this) {
            if (owningsComodity.size() != 0) {
                int idx = (int)(Math.random() * ((owningsComodity.size() - 1) - 0)) + 0;
                Comodity selectedComodity = owningsComodity.get(idx);
                investmentBudget = investmentBudget + (float) selectedComodity.getExchangeRate();
                owningsComodity.remove(owningsComodity.get(idx));
                float percent_max = (float) 0.7 * selectedComodity.getCurrentPrice();
                float percent_min = (float) 0.3 * selectedComodity.getCurrentPrice();
                selectedComodity.setCurrentPrice(selectedComodity.getCurrentPrice() - (float)(Math.random() * (percent_max - percent_min)) + percent_min);
                System.out.println("Investor " + this.nameOfPrInvestor + " sold the comodity called: " + selectedComodity.getNameOfUnit());
                selectedComodity.addToListComodityOfPrices(selectedComodity.getCurrentPrice());
            }
        }
    }

    public void sellCurrency() throws InterruptedException {
        synchronized (this) {
            if (owningsCurrency.size() != 0) {
                int idx = (int)(Math.random() * ((owningsCurrency.size() - 1) - 0)) + 0;
                Currency selectedCurrency = owningsCurrency.get(idx);
                investmentBudget = investmentBudget + selectedCurrency.getExchangeRate();
                owningsCurrency.remove(owningsCurrency.get(idx));
                selectedCurrency.setExchangeRate(selectedCurrency.getExchangeRate() - (float)(Math.random() * (5 - 1)) + 1);
                System.out.println("Investor " + this.nameOfPrInvestor + " sold the currency called: " + selectedCurrency.getNameOfUnit());
                selectedCurrency.addToListCurrencyOfPrices(selectedCurrency.getExchangeRate());
            }
        }
    }

    public void sellStock() throws InterruptedException {
        synchronized (this) {
            if (owningsStocks.size() != 0) {
                int idx = (int)(Math.random() * ((owningsStocks.size() - 1) - 0)) + 0;
                Company selectedStock = owningsStocks.get(idx);
                investmentBudget = investmentBudget + selectedStock.getIPOshareValue();
                owningsStocks.remove(owningsStocks.get(idx));
                float percent_max = (float) 0.3 * selectedStock.getIPOshareValue();
                float percent_min = (float) 0.1 * selectedStock.getIPOshareValue();
                selectedStock.setChanges(selectedStock.getProfit() - selectedStock.getIPOshareValue(), selectedStock.getRevenue() - selectedStock.getIPOshareValue(), selectedStock.getCapital() - selectedStock.getIPOshareValue(), selectedStock.getTotalSales() + 1, selectedStock.getIPOshareValue() - (float)(Math.random() * (percent_max - percent_min)) + percent_min);
                System.out.println("Investor " + this.nameOfPrInvestor + " sold the stock from the company called: " + selectedStock.getNameOfCompany());
                selectedStock.addToListOfPrices(selectedStock.getIPOshareValue());
            }
        }
    }

}

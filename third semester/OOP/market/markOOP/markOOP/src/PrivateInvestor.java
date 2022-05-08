public class PrivateInvestor extends Investor implements Runnable{

    private String firstNameOfPrInvestor;
    private String lastNameOfPrInvestor;

    public String getFirstNameOfPrInvestor() {
        return firstNameOfPrInvestor;
    }
    public String getLastNameOfPrInvestor() {
        return lastNameOfPrInvestor;
    }

    public void setParametersOfPrInvestor(String firstNameOfPrInvestor, String lastNameOfPrInvestor){
        this.firstNameOfPrInvestor = firstNameOfPrInvestor;
        this.lastNameOfPrInvestor = lastNameOfPrInvestor;
    }

    InvestorFund fund = new InvestorFund();
    public void setFund(InvestorFund CurFund){
        fund = CurFund;
    }


    public void buyFundComodity() throws InterruptedException {
        synchronized (this) {
            if (this.getInvestmentBudget() > 0 && fund.owningsComodity.size() != 0) {
                Comodity selectedComodity = fund.owningsComodity.get((int)(Math.random() * ((fund.owningsComodity.size() - 1) - 0)) + 0);
                if (this.getInvestmentBudget() >= selectedComodity.getExchangeRate()) {
                    this.setInvestmentBudget(this.getInvestmentBudget() - (float) selectedComodity.getExchangeRate());
                    fund.setInvestmentBudget(fund.getInvestmentBudget() + (float) selectedComodity.getExchangeRate());
                    owningsComodity.add(selectedComodity);
                    fund.owningsComodity.remove(selectedComodity);
                    float percent_max = (float) 0.8 * selectedComodity.getCurrentPrice();
                    float percent_min = (float) 0.5 * selectedComodity.getCurrentPrice();
                    selectedComodity.setCurrentPrice(selectedComodity.getCurrentPrice() + (float)(Math.random() * (percent_max - percent_min)) + percent_min);
                    System.out.println("Investor " + this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor + " purchased the comodity called: " + selectedComodity.getNameOfUnit() + " through Investment fund");
                    selectedComodity.addToListComodityOfPrices(selectedComodity.getCurrentPrice());
                }
            }
        }
    }


    public void buyFundCurrency() throws InterruptedException {
        synchronized (this) {
            if (this.getInvestmentBudget() > 0 && fund.owningsCurrency.size() != 0) {
                Currency selectedCurrency = fund.owningsCurrency.get((int)(Math.random() * ((fund.owningsCurrency.size() - 1) - 0)) + 0);
                if (this.getInvestmentBudget() >= selectedCurrency.getExchangeRate()) {
                    this.setInvestmentBudget(this.getInvestmentBudget() - selectedCurrency.getExchangeRate());
                    fund.setInvestmentBudget(fund.getInvestmentBudget() + selectedCurrency.getExchangeRate());
                    owningsCurrency.add(selectedCurrency);
                    fund.owningsCurrency.remove(selectedCurrency);
                    selectedCurrency.setExchangeRate(selectedCurrency.getExchangeRate() + (float)(Math.random() * (5 - 1)) + 1);
                    System.out.println("Investor " + this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor + " purchased the currency called: " + selectedCurrency.getNameOfUnit() + " through Investment fund");
                    selectedCurrency.addToListCurrencyOfPrices(selectedCurrency.getExchangeRate());
                }
            }
        }
    }


    public void buyFundStock() throws InterruptedException {
        synchronized (this) {
            if (this.getInvestmentBudget() > 0 && fund.owningsStocks.size() != 0) {
                Company selectedStock = fund.owningsStocks.get((int)(Math.random() * ((fund.owningsStocks.size() - 1) - 0)) + 0);
                if (this.getInvestmentBudget() >= selectedStock.getIPOshareValue() && selectedStock.getTradingVolume() != 0) {
                    this.setInvestmentBudget(this.getInvestmentBudget() - selectedStock.getIPOshareValue());
                    fund.setInvestmentBudget(fund.getInvestmentBudget() + selectedStock.getIPOshareValue());
                    owningsStocks.add(selectedStock);
                    fund.owningsStocks.remove(selectedStock);
                    float percent_max = (float) 0.3 * selectedStock.getIPOshareValue();
                    float percent_min = (float) 0.1 * selectedStock.getIPOshareValue();
                    selectedStock.setChanges(selectedStock.getProfit() + selectedStock.getIPOshareValue(), selectedStock.getRevenue() + selectedStock.getIPOshareValue(), selectedStock.getCapital() + selectedStock.getIPOshareValue(), selectedStock.getTotalSales() + 1, selectedStock.getIPOshareValue() + (float)(Math.random() * (percent_max - percent_min)) + percent_min);
                    System.out.println("Investor " + this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor + " purchased the stock from the company called: " + selectedStock.getNameOfCompany() + " through Investment fund");
                    selectedStock.addToListOfPrices(selectedStock.getIPOshareValue());
                }
            }
        }
    }

    public void sellFundComodity() throws InterruptedException {
        synchronized (this) {
            if (owningsComodity.size() != 0) {
                int idx = (int)(Math.random() * ((owningsComodity.size() - 1) - 0)) + 0;
                Comodity selectedComodity = owningsComodity.get(idx);
                this.setInvestmentBudget(this.getInvestmentBudget() + (float) selectedComodity.getExchangeRate());
                fund.setInvestmentBudget(fund.getInvestmentBudget() - (float) selectedComodity.getExchangeRate());
                fund.owningsComodity.add(owningsComodity.get(idx));
                owningsComodity.remove(owningsComodity.get(idx));
                float percent_max = (float) 0.7 * selectedComodity.getCurrentPrice();
                float percent_min = (float) 0.3 * selectedComodity.getCurrentPrice();
                selectedComodity.setCurrentPrice(selectedComodity.getCurrentPrice() - (float)(Math.random() * (percent_max - percent_min)) + percent_min);
                System.out.println("Investor " + this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor + " sold the comodity called: " + selectedComodity.getNameOfUnit() + " through Investment fund");
                selectedComodity.addToListComodityOfPrices(selectedComodity.getCurrentPrice());
            }
        }
    }

    public void sellFundCurrency() throws InterruptedException {
        synchronized (this) {
            if (owningsCurrency.size() != 0) {
                int idx = (int)(Math.random() * ((owningsCurrency.size() - 1) - 0)) + 0;
                Currency selectedCurrency = owningsCurrency.get(idx);
                this.setInvestmentBudget(this.getInvestmentBudget() + selectedCurrency.getExchangeRate());
                fund.setInvestmentBudget(fund.getInvestmentBudget() - selectedCurrency.getExchangeRate());
                fund.owningsCurrency.add(owningsCurrency.get(idx));
                owningsCurrency.remove(owningsCurrency.get(idx));
                selectedCurrency.setExchangeRate(selectedCurrency.getExchangeRate() - (float)(Math.random() * (5 - 1)) + 1);
                System.out.println("Investor " + this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor + " sold the currency called: " + selectedCurrency.getNameOfUnit() + " through Investment fund");
                selectedCurrency.addToListCurrencyOfPrices(selectedCurrency.getExchangeRate());
            }
        }
    }

    public void sellFundStock() throws InterruptedException {
        synchronized (this) {
            if (owningsStocks.size() != 0) {
                int idx = (int)(Math.random() * ((owningsStocks.size() - 1) - 0)) + 0;
                Company selectedStock = owningsStocks.get(idx);
                this.setInvestmentBudget(this.getInvestmentBudget() + selectedStock.getIPOshareValue());
                fund.setInvestmentBudget(fund.getInvestmentBudget() - selectedStock.getIPOshareValue());
                fund.owningsStocks.add(owningsStocks.get(idx));
                owningsStocks.remove(owningsStocks.get(idx));
                float percent_max = (float) 0.3 * selectedStock.getIPOshareValue();
                float percent_min = (float) 0.1 * selectedStock.getIPOshareValue();
                selectedStock.setChanges(selectedStock.getProfit() - selectedStock.getIPOshareValue(), selectedStock.getRevenue() - selectedStock.getIPOshareValue(), selectedStock.getCapital() - selectedStock.getIPOshareValue(), selectedStock.getTotalSales() + 1, selectedStock.getIPOshareValue() - (float)(Math.random() * (percent_max - percent_min)) + percent_min);
                System.out.println("Investor " + this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor + " sold the stock from the company called: " + selectedStock.getNameOfCompany() + " through Investment fund");
                selectedStock.addToListOfPrices(selectedStock.getIPOshareValue());
            }
        }
    }


    public void run(){
        while(true){
            try {
                if ((int)(Math.random() * ((100 - 0) + 0)) > 25){
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    this.setNameOfPrInvestor(this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor);
                    buyComodity();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    this.setNameOfPrInvestor(this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor);
                    buyCurrency();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    this.setNameOfPrInvestor(this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor);
                    buyStock();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                   this.setNameOfPrInvestor(this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor);
                    sellCurrency();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    this.setNameOfPrInvestor(this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor);
                    sellStock();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    this.setNameOfPrInvestor(this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor);
                    sellComodity();
                }
                else{
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    buyFundComodity();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    buyFundCurrency();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    buyFundStock();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    sellFundCurrency();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    sellFundStock();
                    Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                    sellFundComodity();
                }
                Thread.sleep((int)(Math.random() * (1000 - 500)) + 500);
                increaseInvestmentBudget();
                System.out.println("Investor " + this.firstNameOfPrInvestor + " " + this.lastNameOfPrInvestor + " raised their budget.");
            } catch(InterruptedException exception){
                Thread.currentThread().interrupt();
            }
        }
    }
}

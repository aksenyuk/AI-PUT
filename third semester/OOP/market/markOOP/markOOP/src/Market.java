public abstract class Market {
    private String nameOfMarket;
    private String country;
    private String tradingUnit;
    private String city;
    private String address;
    private int percentageMargin;
    private int transactionMargin;
    public String getNameOfMarket(){
        return nameOfMarket;
    }
    public String getCountry(){
        return country;
    }
    public String getTradingUnit(){
        return tradingUnit;
    }
    public String getCity(){
        return city;
    }
    public String getAddress(){
        return address;
    }
    public int getPercentageMargin(){ return percentageMargin; }
    public int getTransactionMargin(){
        return transactionMargin;
    }

    public void setParametersOfMarket(String nameOfMarket, String country, String city, String address, int percentageMargin, int transactionMargin){
        this.nameOfMarket = nameOfMarket;
        this.country = country;
        this.city = city;
        this.address = address;
        this.percentageMargin = percentageMargin;
        this.transactionMargin = transactionMargin;
    }
}

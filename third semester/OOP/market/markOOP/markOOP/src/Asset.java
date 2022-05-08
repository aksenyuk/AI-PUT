public class Asset {

    private String nameOfUnit;
    private float minPrice;
    private float maxPrice;
    private float currentPrice;

    public float getMinPrice(){
        return minPrice;
    }
    public float getMaxPrice() {
        return maxPrice;
    }
    public float getCurrentPrice(){
        return currentPrice;
    }

    public String getNameOfUnit() { return nameOfUnit; }

    public void setPrices(float minPrice, float maxPrice, float currentPrice){
        this.minPrice = minPrice;
        this.maxPrice = maxPrice;
        this.currentPrice = currentPrice;
    }

    public void setCurrentPrice(float currentPrice){
        this.currentPrice = currentPrice;
    }

    public void setNameOfUnit(String nameOfUnit){
        this.nameOfUnit = nameOfUnit;
    }


}

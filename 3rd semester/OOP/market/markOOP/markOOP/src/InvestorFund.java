import java.lang.Thread;

public class InvestorFund extends Investor implements Runnable{

    private String nameOfManager;
    private String lastNameOfManager;

    public String getNameOfManager() {
        return nameOfManager;
    }

    public String getLastNameOfManager() {
        return lastNameOfManager;
    }
    public void setParametersOfInvestorFund(String nameOfManager, String lastNameOfManager){
        this.lastNameOfManager = lastNameOfManager;
        this.nameOfManager = nameOfManager;
    }

    public void run(){
        while(true){
            try {
                Thread.sleep((int)(Math.random() * ((1000 - 500) + 500)));
                this.setNameOfPrInvestor("fund manager " + this.nameOfManager + " " + this.lastNameOfManager);
                buyComodity();
                Thread.sleep((int)(Math.random() * ((1000 - 500) + 500)));
                this.setNameOfPrInvestor("fund manager " + this.nameOfManager + " " + this.lastNameOfManager);
                buyCurrency();
                Thread.sleep((int)(Math.random() * ((1000 - 500) + 500)));
                this.setNameOfPrInvestor("fund manager " + this.nameOfManager + " " + this.lastNameOfManager);
                buyStock();
                Thread.sleep((int)(Math.random() * ((1000 - 500) + 500)));
                increaseInvestmentBudget();
                Thread.sleep((int)(Math.random() * ((1000 - 500) + 500)));
                this.setNameOfPrInvestor("fund manager " + this.nameOfManager + " " + this.lastNameOfManager);
                sellCurrency();
                Thread.sleep((int)(Math.random() * ((1000 - 500) + 500)));
                this.setNameOfPrInvestor("fund manager " + this.nameOfManager + " " + this.lastNameOfManager);
                sellStock();
                Thread.sleep((int)(Math.random() * ((1000 - 500) + 500)));
                this.setNameOfPrInvestor("fund manager " + this.nameOfManager + " " + this.lastNameOfManager);
                sellComodity();
            } catch(InterruptedException exception){
                Thread.currentThread().interrupt();
            }
        }
    }

}

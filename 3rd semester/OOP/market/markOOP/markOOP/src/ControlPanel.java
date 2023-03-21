import javax.swing.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class ControlPanel extends JFrame{

    private JButton button1;
    private JPanel panel1;
    private JTextField textField1;

    private int noOfAssets;

    public ControlPanel(String title) {
        super(title);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(panel1);
        this.pack();

        setBounds(200, 200, 400, 400);

        button1.addActionListener(e -> {
            this.noOfAssets = Integer.parseInt(textField1.getText());
            System.out.println(noOfAssets);
            mark();
            this.setVisible(false);
            JFrame assets = new AssetsPanel("Assets", comodities, currencies, companies);
            assets.setVisible(true);
        });

    }


    public static void main(String[] args) {
        JFrame control = new ControlPanel("Market");
        control.setVisible(true);
    }



    ArrayList<Company> companies = new ArrayList();
    ArrayList<Comodity> comodities = new ArrayList<>();
    ArrayList<Currency> currencies = new ArrayList<>();

    public void mark(){
        List<String> currencies = Arrays.asList("USD", "EUR", "RUB", "UAH", "PLN", "PUT");
        List<String> units = Arrays.asList("piwo", "paliwo", "plants", "bread", "milk", "gas", "oil", "eggs", "meat", "funny calendars", "super facet merch");
        List<String> names = Arrays.asList("Liam", "Emma", "Oliver", "Benjamin", "Mia", "William", "Investor", "Scot", "Maciej", "Kurt", "Leo");
        List<String> surnames = Arrays.asList("Miller", "Rodriguez", "John", "Martin", "Clark", "Stallone", "Scott", "Hill", "Cobain", "Morris", "Parker");
        ComodityMarket marketOfComodities = new ComodityMarket();
        CurrencyMarket marketOfCurrencies = new CurrencyMarket();
        StockMarket marketOfStocks = new StockMarket();

        marketOfStocks.setParametersOfMarket("Stock Market", "USA", "California", "Laurel 11", (int)(Math.random() * (550 - 200)) + 200, (int)(Math.random() * (600 - 250)) + 250);
        marketOfCurrencies.setParametersOfMarket("Currency Market", "France", "Paris", "Quai Saint-Bernand 8", (int)(Math.random() * (70 - 40)) + 40, (int)(Math.random() * (55 - 20)) + 20);
        marketOfComodities.setParametersOfMarket("Comodity Market", "Poland", "Bydgoszcz", "Jana Pawla II 1", (int)(Math.random() * (10 - 3)) + 3, (int)(Math.random() * (10 - 3)) + 3);

        ArrayList<Index>indeces = new ArrayList();
        for (int i = 0; i < noOfAssets / 4; i++) {
            Index idx = new Index();
            idx.setIndexValue(i);
            marketOfStocks.addToListOfIndexes(idx);
            indeces.add(idx);
        }

        ArrayList<InvestorFund>invFund = new ArrayList();
        ArrayList<PrivateInvestor>prInvestor = new ArrayList();
        for (int i = 0; i < noOfAssets / 3; i++){
            InvestorFund investor = new InvestorFund();
            investor.setInvestmentBudget((int)(Math.random() * (10000000 - 3000000)) + 3000000);
            investor.setParametersOfInvestorFund(names.get((int)(Math.random() * ((names.size() - 1) - 0)) + 0), surnames.get((int)(Math.random() * ((surnames.size() - 1) - 0)) + 0));
            invFund.add(investor);

            PrivateInvestor privInvestor = new PrivateInvestor();
            privInvestor.setInvestmentBudget((int)(Math.random() * (10000000 - 3000000)) + 3000000);
            privInvestor.setParametersOfPrInvestor(names.get((int)(Math.random() * ((names.size() - 1) - 0)) + 0), surnames.get((int)(Math.random() * ((surnames.size() - 1) - 0)) + 0));
            prInvestor.add(privInvestor);
        }

        for (int i = 0; i < noOfAssets / 3; i++){
            Comodity com = new Comodity();
            com.setPrices((int)(Math.random() * (15000 - 10000)) + 10000, (int)(Math.random() * (15000 - 10000)) + 10000, (int)(Math.random() * (15000 - 10000)) + 10000);
            com.setNameOfUnit(units.get((int)(Math.random() * ((units.size() - 1) - 0)) + 0));
            com.setExchangeRate((int)(Math.random() * (6 - 2)) + 2);
            marketOfComodities.addToListOfComodities(com);
            this.comodities.add(com);
            Currency cur = new Currency();
            cur.setPrices(50, 120, 80);
            cur.setExchangeRate((int)(Math.random() * (120 - 80)) + 80);
            marketOfCurrencies.addToListOfCurrencies(cur);
            cur.setNameOfUnit(currencies.get((int)(Math.random() * ((currencies.size() - 1) - 0)) + 0));
            this.currencies.add(cur);
            Company comp = new Company();
            Random rnd = new Random();
            int day = (int)(Math.random() * (30 - 1)) + 1;
            int month = (int)(Math.random() * (12 - 1)) + 1;
            int year = (int)(Math.random() * (2020 - 1990)) + 1990;
            String date = day + "." + month + "." + year;
            comp.setParametersOfCompany((String)((char)('A' + rnd.nextInt(26)) + "-company"), date, (int)(Math.random() * (100 - 10)) + 10, (int)(Math.random() * (1000000 - 100000)) + 1000000, (int)(Math.random() * (3000000 - 500000)) + 500000, (int)(Math.random() * (2000000 - 300000)) + 300000, (int)(Math.random() * (7000000 - 3000000)) + 3000000, (int)(Math.random() * (100 - 10)) + 10, (int)(Math.random() * (100 - 10)) + 10);
            this.companies.add(comp);
            Index idx = indeces.get((int)(Math.random() * ((indeces.size() - 1) - 0)) + 0);
            idx.addToListOfCompanies(comp);
            InvestorFund fund = invFund.get((int)(Math.random() * ((invFund.size() - 1) - 0)) + 0);
            fund.setAvailableComodities(com);
            fund.setAvailableCurrencies(cur);
            fund.setAvailableStocks(comp);
            PrivateInvestor inv = prInvestor.get((int)(Math.random() * ((prInvestor.size() - 1) - 0)) + 0);
            inv.setAvailableComodities(com);
            inv.setAvailableCurrencies(cur);
            inv.setAvailableStocks(comp);
            inv.setFund(fund);
        }


        prInvestor.forEach(investor -> new Thread(investor).start());
        invFund.forEach(investor -> new Thread(investor).start());
        marketOfStocks.getlistOfIndexes().forEach(idx -> idx.getListOfCompanies().forEach(company -> new Thread(company).start()));


    }

    public ArrayList<Company> getCompanies(){
        return companies;
    }

    public ArrayList<Comodity> getComodities(){
        return comodities;
    }

        public ArrayList<Currency> getCurrencies(){
        return currencies;
    }
}

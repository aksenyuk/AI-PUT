import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AssetsPanel extends JFrame{
    private JPanel panel1;
    DefaultListModel modelCom = new DefaultListModel();
    private JList comodities;
    DefaultListModel modelCur = new DefaultListModel();
    private JList currencies;
    DefaultListModel modelStock = new DefaultListModel();
    private JList stocks;


    public AssetsPanel(String title,  ArrayList<Comodity> com, ArrayList<Currency> cur, ArrayList<Company> comp) {
        super(title);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(panel1);
        this.pack();

        setBounds(400, 400, 600, 600);

        for(int i = 0; i < com.size(); i++){
            String name = com.get(i).getNameOfUnit();
            modelCom.addElement(name);
        }
        comodities.setModel(modelCom);

        for(int i = 0; i < cur.size(); i++){
            String name = cur.get(i).getNameOfUnit();
            modelCur.addElement(name);
        }
        currencies.setModel(modelCur);

        for(int i = 0; i < comp.size(); i++){
            String name = comp.get(i).getNameOfCompany();
            modelStock.addElement(name + "'s stock");
        }
        stocks.setModel(modelStock);

        stocks.addListSelectionListener(e -> {
            if (e.getValueIsAdjusting() == false) {
                for(int i = 0; i < comp.size(); i++){
                    String name = comp.get(i).getNameOfCompany() + "'s stock";
                    if ((name).equals(stocks.getSelectedValue())){
                        List<Double> prices = new ArrayList<Double>(comp.get(i).getListOfPrices());
                        SwingUtilities.invokeLater(() -> GraphPanel.plotGraph(prices, name));
                        ArrayList<String> data = new ArrayList<String>();
                        ArrayList<String> nazwa = new ArrayList<String>();
                        data.add(comp.get(i).getIPOdate());
                        nazwa.add("IPO date");
                        data.add(String.valueOf(comp.get(i).getIPOshareValue()));
                        nazwa.add("IPO share value");
                        data.add(String.valueOf(comp.get(i).getOpeningPrice()));
                        nazwa.add("Opening price");
                        data.add(String.valueOf(comp.get(i).getTotalSales()));
                        nazwa.add("Total sales");
                        data.add(String.valueOf(comp.get(i).getTradingVolume()));
                        nazwa.add("Trading volume");
                        JFrame dataPanel = new DataPanel("Data", data, nazwa);
                        dataPanel.setVisible(true);
                    }
                }
            }
        });

        comodities.addListSelectionListener(e -> {
            if (e.getValueIsAdjusting() == false) {
                for(int i = 0; i < com.size(); i++){
                    String name = com.get(i).getNameOfUnit();
                    if ((name).equals(comodities.getSelectedValue())){
                        List<Double> prices = new ArrayList<Double>(com.get(i).getListOfComodityPrices());
                        SwingUtilities.invokeLater(() -> GraphPanel.plotGraph(prices, name));
                        ArrayList<String> data = new ArrayList<String>();
                        ArrayList<String> nazwa = new ArrayList<String>();
                        data.add(String.valueOf(com.get(i).getExchangeRate()));
                        nazwa.add("Exchange rate");
                        data.add(String.valueOf(com.get(i).getCurrentPrice()));
                        nazwa.add("Current Price");
                        data.add(String.valueOf(com.get(i).getMaxPrice()));
                        nazwa.add("Maximum price");
                        data.add(String.valueOf(com.get(i).getMinPrice()));
                        nazwa.add("Minimum price");
                        JFrame dataPanel = new DataPanel("Data", data, nazwa);
                        dataPanel.setVisible(true);
                    }
                }
            }
        });

        currencies.addListSelectionListener(e -> {
            if (e.getValueIsAdjusting() == false) {
                for(int i = 0; i < cur.size(); i++){
                    String name = cur.get(i).getNameOfUnit();
                    if ((name).equals(currencies.getSelectedValue())){
                        List<Double> prices = new ArrayList<Double>(cur.get(i).getListOfCurrencyPrices());
                        SwingUtilities.invokeLater(() -> GraphPanel.plotGraph(prices, name));
                        ArrayList<String> data = new ArrayList<String>();
                        ArrayList<String> nazwa = new ArrayList<String>();
                        data.add(String.valueOf(com.get(i).getExchangeRate()));
                        nazwa.add("Exchange rate");
                        data.add(String.valueOf(com.get(i).getCurrentPrice()));
                        nazwa.add("Current Price");
                        data.add(String.valueOf(com.get(i).getMaxPrice()));
                        nazwa.add("Maximum price");
                        data.add(String.valueOf(com.get(i).getMinPrice()));
                        nazwa.add("Minimum price");
                        JFrame dataPanel = new DataPanel("Data", data, nazwa);
                        dataPanel.setVisible(true);
                    }
                }
            }
        });




    }

}

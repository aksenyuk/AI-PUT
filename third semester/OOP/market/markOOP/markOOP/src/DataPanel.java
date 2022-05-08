import javax.swing.*;
import java.util.ArrayList;

public class DataPanel extends JFrame{
    private JPanel panel1;
    DefaultListModel modelData = new DefaultListModel();
    private JList list1;
    DefaultListModel modelNazwy = new DefaultListModel();
    private JList list2;

    public DataPanel(String title, ArrayList<String> data, ArrayList<String> nazwy){
        super(title);

        this.setContentPane(panel1);
        this.pack();

        setBounds(200, 200, 400, 400);
        for(int i = 0; i < data.size(); i++){
            modelData.addElement(data.get(i));
        }
        list2.setModel(modelData);

        for(int i = 0; i < nazwy.size(); i++){
            modelNazwy.addElement(nazwy.get(i));
        }
        list1.setModel(modelNazwy);
    }
}

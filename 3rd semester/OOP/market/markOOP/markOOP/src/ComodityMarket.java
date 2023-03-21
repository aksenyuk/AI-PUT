import java.util.*;

public class ComodityMarket extends Market{
//    Collection<Comodity>listOfComodities = new ArrayList();
    ArrayList<Comodity>listOfComodities = new ArrayList();

    public ArrayList<Comodity> getListOfComodities() { return listOfComodities; }
    public void addToListOfComodities(Comodity comodity){
        listOfComodities.add(comodity);
    }
}

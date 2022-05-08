import java.util.*;

public class Index {
    private int indexValue;
    Collection<Company>listOfCompanies = new ArrayList();

    public int getIndexValue(){
        return indexValue;
    }
    public void setIndexValue(int indexValue){
        this.indexValue = indexValue;
    }
    public Collection<Company> getListOfCompanies() { return listOfCompanies; }
    public void addToListOfCompanies(Company company){
        listOfCompanies.add(company);
    }
}

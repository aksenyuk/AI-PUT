import java.util.*;

public class StockMarket extends Market{
    Collection<Index>listOfIndexes = new ArrayList();
    public void addToListOfIndexes(Index idx){
        listOfIndexes.add(idx);
    }
    public Collection<Index> getlistOfIndexes() { return listOfIndexes; }
}

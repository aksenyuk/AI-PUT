import java.util.*;

public class CurrencyMarket extends Market{
    Collection<Currency> listOfCurrencies = new ArrayList();
    public Collection<Currency> getListOfCurrencies() { return listOfCurrencies; }
    public void addToListOfCurrencies(Currency currency){
        listOfCurrencies.add(currency);
    }
}

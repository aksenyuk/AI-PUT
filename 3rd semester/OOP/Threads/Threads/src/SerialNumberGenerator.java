// Materiały zaczerpnięte z 'Thinking in Java, 3rd ed.' (c)
// Bruce Eckel 2002 www.BruceEckel.com.

public class SerialNumberGenerator {
  private static volatile int serialNumber = 0;
  public synchronized static int nextSerialNumber() {
    return serialNumber++;
  }
}

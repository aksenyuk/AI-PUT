// Code examples taken by DB from 'Thinking in Java, 3rd ed.' (c)
// Bruce Eckel 2002 www.BruceEckel.com.

class CircularSet {

    private int[] array;
    private int len;
    private int index = 0;

    public CircularSet(int size) {
        array = new int[size];
        len = size;

        for (int i = 0; i < size; i++) {
            array[i] = -1;
        }
    }

    public synchronized void add(int i) {
        array[index] = i;
        index = ++index % len;
    }

    public synchronized boolean contains(int val) {
        for (int i = 0; i < len; i++) {
            if (array[i] == val) {
                return true;
            }
        }
        return false;
    }
}

public class SerialNumberChecker {

    private static CircularSet serials = new CircularSet(1000);

    static class SerialChecker extends Thread {

        SerialChecker() {
            start();
        }

        public void run() {
            while (true) {
                int serial =
                        SerialNumberGenerator.nextSerialNumber();
                if (serials.contains(serial)) {
                    System.out.println("Duplicate: " + serial);
                    System.exit(0);
                }
                serials.add(serial);
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            new SerialChecker();
        }
        // Stop after 4 seconds (unless something bad happens earlier...)
        new Timeout(4000, "No duplicates detected");
    }
}

// Code examples taken by DB from 'Thinking in Java, 3rd ed.' (c)
// Bruce Eckel 2002 www.BruceEckel.com.

/**
 * A class showing what happens when multiple threads can access the 
 * same variable
 */
public class AlwaysEven {

    /**
     * Variable hosting an even number.
     */
    private int i;
    private Object killer = new Object();
    /**
     * Method for incrementing the state by 2.
     */
    public void next() {
        synchronized(killer) {
            i++;
            i++;
        }
    }

    /**
     * Returns the current value of i.
     * @return an even number?
     */
    public synchronized int getValue(){
        synchronized(killer) {
            return i;
        }
    }

    /**
     * Main method
     * @param args
     */
    public static void main(String[] args) {
        final AlwaysEven ae = new AlwaysEven();

        // Here we're creating a thread that checks if the number is even
        // Where's Chuck? Where's the disco? Are you sure?
        new Thread("Watcher") {

            public void run() {
                while (true) {
                    int val = ae.getValue();
                    if (val % 2 != 0) {
                        System.out.println("wrong: " + val);
                        System.exit(0);
                    }
                }
            }
        }.start();

        // A loop that keeps generating even numbers
        while (true) {
            ae.next();
        }
    }
}


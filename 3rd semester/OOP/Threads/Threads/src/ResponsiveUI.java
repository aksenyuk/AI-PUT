// Code examples taken by DB from 'Thinking in Java, 3rd ed.' (c)
// Bruce Eckel 2002 www.BruceEckel.com.

class UnresponsiveUI {

    private volatile double d = 1;

    public UnresponsiveUI() throws Exception {
        while (d > 0) {
            d = d + (Math.PI + Math.E) / d;
        }
        System.in.read(); // We might never get here...
    }
}

public class ResponsiveUI extends Thread {

    private static volatile double d = 1;

    public ResponsiveUI() {
        setDaemon(true);
        start();
    }

    public void run() {
        while (true) {
            d = d + (Math.PI + Math.E) / d;
        }
    }

    public static void main(String[] args) throws Exception {
        //! new UnresponsiveUI(); // If you uncomment this lone, you will have to kill the program manually
        new ResponsiveUI();
        Thread.sleep(300);
        System.in.read();
        System.out.println(d);
    }
}


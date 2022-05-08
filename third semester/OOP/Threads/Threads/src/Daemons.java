// Code examples taken by DB from 'Thinking in Java, 3rd ed.' (c)
// Bruce Eckel 2002 www.BruceEckel.com.

import java.io.*;

/**
 * A class showing what daemon threads are all about.
 * @author Dabrze
 */
class Daemon extends Thread {

    private Thread[] t = new Thread[10];

    public Daemon() {
        // setting a thread to be a daemon (weak) thread
        setDaemon(true);
        start();
    }

    public void run() {
        // let's spawn 10 deamons
        for (int i = 0; i < t.length; i++) {
            t[i] = new DaemonSpawn(i);
        }
        for (int i = 0; i < t.length; i++) {
            System.out.println("t[" + i + "].isDaemon() = " + t[i].isDaemon());
        }
        while (true) {
            Thread.yield();
        }
    }
}

class DaemonSpawn extends Thread {

    public DaemonSpawn(int i) {
        start();
        System.out.println("DaemonSpawn " + i + " started");
    }

    public void run() {
        while (true) {
            Thread.yield();
        }
    }
}

public class Daemons {

    public static void main(String[] args) throws Exception {
        Thread d = new Daemon();
        System.out.println("d.isDaemon() = " + d.isDaemon());

        // End the main thread after 1 second
        Thread.sleep(1000);
    }
}


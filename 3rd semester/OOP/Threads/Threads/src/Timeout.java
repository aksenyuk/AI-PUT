// Code examples taken by DB from 'Thinking in Java, 3rd ed.' (c)
// Bruce Eckel 2002 www.BruceEckel.com.

import java.util.*;

public class Timeout extends Timer {
  public Timeout(int delay, final String msg) {
    super(true); // Daemon thread
    schedule(new TimerTask() {
      public void run() {
        System.out.println(msg);
        System.exit(0);
      }
    }, delay);
  }
}

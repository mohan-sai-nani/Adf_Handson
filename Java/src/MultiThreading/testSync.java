package MultiThreading;


class SyncCounter extends Thread {
    int count = 0;
    public synchronized void run()
    {
        int max = 1_000_00_000;
        for (int i = 0; i < max; i++) {
            count++;
        }
    }
}

public class testSync {
    public static void main(String[] args) throws InterruptedException {
        Counter c = new Counter();
        SyncCounter sc = new SyncCounter();

        Thread first = new Thread(c, "First");
        Thread second = new Thread(c, "Second");
        Thread third = new Thread(sc, "Third");
        Thread fourth = new Thread(sc, "Fourth");

        first.start();
        second.start();
        third.start();
        fourth.start();

        first.join();
        second.join();
        third.join();
        fourth.join();

        System.out.println("Using Standard Int: " + c.count);
        System.out.println("Using Synchronized: " + sc.count);
    }
}

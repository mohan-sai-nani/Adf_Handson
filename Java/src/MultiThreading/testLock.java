package MultiThreading;

import java.util.concurrent.locks.ReentrantLock;

class useLockCounter extends Thread {
    private final ReentrantLock lock = new ReentrantLock ();
    int count = 0;
    public void run()
    {
        int max = 1_000_00_000;
        for (int i = 0; i < max; i++) {
            lock.lock();
            count++;
            lock.unlock();
        }
    }
}

public class testLock {
    public static void main(String[] args) throws InterruptedException {
        Counter c = new Counter();
        useLockCounter lc = new useLockCounter();

        Thread first = new Thread(c, "First");
        Thread second = new Thread(c, "Second");
        Thread third = new Thread(lc, "Third");
        Thread fourth = new Thread(lc, "Fourth");

        first.start();
        second.start();
        third.start();
        fourth.start();

        first.join();
        second.join();
        third.join();
        fourth.join();

        System.out.println("Using Standard Int: " + c.count);
        System.out.println("Using Lock: " + lc.count);
    }
}


package MultiThreading;

import java.util.concurrent.atomic.AtomicInteger;

class AtomicCounter extends Thread {
    AtomicInteger count;
    AtomicCounter()
    {
        count = new AtomicInteger();
    }
    public void run()
    {
        int max = 1_000_00_000;
        for (int i = 0; i < max; i++) {
            count.addAndGet(1);
        }
    }
}

class Counter extends Thread {
    int count = 0;
    public void run()
    {
        int max = 1_000_00_000;
        for (int i = 0; i < max; i++) {
            count++;
        }
    }
}

public class testAtomicVariable {
    public static void main(String[] args) throws InterruptedException {
        Counter c = new Counter();
        AtomicCounter ac = new AtomicCounter();

        Thread first = new Thread(c, "First");
        Thread second = new Thread(c, "Second");
        Thread third = new Thread(ac, "Third");
        Thread fourth = new Thread(ac, "Fourth");

        first.start();
        second.start();
        third.start();
        fourth.start();

        first.join();
        second.join();
        third.join();
        fourth.join();

        System.out.println("Using Standard Int: " + c.count);
        System.out.println("Using Atomic Int: " + ac.count);
    }
}

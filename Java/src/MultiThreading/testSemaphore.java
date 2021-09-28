package MultiThreading;
import java.util.concurrent.*;

class Shared {
    static int count = 0;
}

class NormalThread extends Thread{
    String threadName;
    public NormalThread(String threadName) {
        super(threadName);
        this.threadName = threadName;
    }
    public void run(){
        if (this.getName().equals("A")){
            for(int i=0; i < 5; i++) {
                Shared.count++;
                System.out.println(threadName + ": " + Shared.count);
                try {
                    Thread.sleep(10);
                }
                catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
        else {
            for(int i=0; i < 5; i++) {
                Shared.count--;
                System.out.println(threadName + ": " + Shared.count);
                try {
                    Thread.sleep(10);
                }
                catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

class SemaphoreThread extends Thread {
    Semaphore sem;
    String threadName;
    public SemaphoreThread(Semaphore sem, String threadName) {
        super(threadName);
        this.sem = sem;
        this.threadName = threadName;
    }
    @Override
    public void run() {
        if(this.getName().equals("A")) {
            System.out.println("Starting " + threadName);
            try {
                System.out.println(threadName + " is waiting for a permit.");
                sem.acquire();
                System.out.println(threadName + " gets a permit.");
                for(int i=0; i < 5; i++) {
                    Shared.count++;
                    System.out.println(threadName + ": " + Shared.count);
                    Thread.sleep(10);
                }
            }
            catch (InterruptedException exc) {
                System.out.println(exc);
            }
            System.out.println(threadName + " releases the permit.");
            sem.release();
        }
        else {
            System.out.println("Starting " + threadName);
            try {
                System.out.println(threadName + " is waiting for a permit.");
                sem.acquire();
                System.out.println(threadName + " gets a permit.");
                for(int i=0; i < 5; i++) {
                    Shared.count--;
                    System.out.println(threadName + ": " + Shared.count);
                    Thread.sleep(10);
                }
            }
            catch (InterruptedException exc) {
                System.out.println(exc);
            }
            System.out.println(threadName + " releases the permit.");
            sem.release();
        }
    }
}


public class testSemaphore {
    public static void main(String args[]) throws InterruptedException {
        Semaphore sem = new Semaphore(1);
        SemaphoreThread st1 = new SemaphoreThread(sem, "A");
        SemaphoreThread st2 = new SemaphoreThread(sem, "B");


        st1.start();
        st2.start();

        st1.join();
        st2.join();
        System.out.println("After SemaphoreCount: " + Shared.count);

        NormalThread nt1 = new NormalThread("A");
        NormalThread nt2 = new NormalThread("B");

        nt1.start();
        nt2.start();

        nt1.join();
        nt2.join();

        System.out.println("After NormalCount: " + Shared.count);
    }
}
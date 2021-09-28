package MultiThreading;
import java.util.concurrent.*;

class SyncThread extends Thread{
    String threadName;
    public SyncThread(String threadName) {
        super(threadName);
        this.threadName = threadName;
    }
    public synchronized void run(){
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


public class testSyncFail {
    public static void main(String args[]) throws InterruptedException {
        Semaphore sem = new Semaphore(1);
        SemaphoreThread st1 = new SemaphoreThread(sem, "A");
        SemaphoreThread st2 = new SemaphoreThread(sem, "B");

        st1.start();
        st2.start();

        st1.join();
        st2.join();
        System.out.println("After SemaphoreCount: " + Shared.count);

        SyncThread syt1 = new SyncThread("A");
        SyncThread syt2 = new SyncThread("B");

        syt1.start();
        syt2.start();

        syt1.join();
        syt2.join();

        System.out.println("After SyncCount: " + Shared.count);
    }
}
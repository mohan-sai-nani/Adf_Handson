package MultiThreading;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class WorkerThread implements Runnable {
    private String message;
    public WorkerThread(String s){
        this.message = s;
    }

    public void run() {
        Date d = new Date();
        SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss");
        System.out.println(Thread.currentThread().getName()+" (Start) message = "+message+" Time:"+ft.format(d));
        processMessage();
        System.out.println(Thread.currentThread().getName()+" (End)"+" Time:"+ft.format(d));
    }

    private void processMessage() {
        try {  Thread.sleep(5000);  } catch (InterruptedException e) { e.printStackTrace(); }
    }

}


public class testThreadPool {
    static void test(int threads, int tasks){
        ExecutorService executor = Executors.newFixedThreadPool(threads);
        for (int i = 0; i < tasks; i++) {
            Runnable worker = new WorkerThread("" + i);
            executor.execute(worker);
        }
        executor.shutdown();
        while (!executor.isTerminated()) {
        }
        System.out.println("Finished all threads");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of threads: ");
        int threads = sc.nextInt();
        System.out.println("Enter the number of tasks: ");
        int tasks = sc.nextInt();
        test(threads, tasks);
    }

}
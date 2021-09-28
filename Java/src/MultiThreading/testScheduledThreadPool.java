package MultiThreading;
import java.util.*;
import java.util.concurrent.*;
import java.io.*;

public class testScheduledThreadPool {
    public static void main(String[] args)
    {
        ScheduledThreadPoolExecutor threadPool = new ScheduledThreadPoolExecutor(2);
        Runnable task1 = new Command("task1");
        Runnable task2 = new Command("task2");
        System.out.println("Current time:" + Calendar.getInstance().get(Calendar.SECOND));
        threadPool.scheduleAtFixedRate(task1, 2, 8, TimeUnit.SECONDS);
        threadPool.scheduleWithFixedDelay(task2, 5, 5, TimeUnit.SECONDS);
        try {
            Thread.sleep(30000);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        threadPool.shutdown();
    }
}

class Command implements Runnable {
    String taskName;
    public Command(String taskName)
    {
        this.taskName = taskName;
    }
    public void run()
    {
        try {
            System.out.println("Task name : " + this.taskName + " Current time : " + Calendar.getInstance().get(Calendar.SECOND));
            Thread.sleep(2000);
            System.out.println("Executed : " + this.taskName + " Current time : " + Calendar.getInstance().get(Calendar.SECOND));
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}

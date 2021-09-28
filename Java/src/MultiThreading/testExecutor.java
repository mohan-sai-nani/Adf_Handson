package MultiThreading;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class testExecutor {

    public static void main(final String[] arguments) throws InterruptedException {
        Executor executor = Executors.newCachedThreadPool();
        executor.execute(new Task());
        ThreadPoolExecutor pool = (ThreadPoolExecutor)executor;
        pool.shutdown();
    }

    static class Task implements Runnable {

        public void run() {

            try {
                long duration = (long) (Math.random() * 5);
                System.out.println("Running Task!");
                System.out.println("Duration:" + duration);
                TimeUnit.SECONDS.sleep(duration);
                System.out.println("Task Completed");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

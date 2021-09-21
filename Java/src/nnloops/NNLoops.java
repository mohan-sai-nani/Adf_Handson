package nnloops;

import java.util.Random;
import java.util.Scanner;

public class NNLoops {

    void oneToTen() {
        System.out.println("OneToTen");
        for (int i = 1; i < 11; i++)
            System.out.println(i);
    }

    void oddNumbers() {
        System.out.println("OddNumbers");
        for (int i = 1; i < 20; i += 2)
            System.out.println(i);
    }

    void squares() {
        System.out.println("squares");
        for (int i = 1; i < 11; i++)
            System.out.println(i * i);
    }

    void random4() {
        System.out.println("random4");
        Random random = new Random();
        for (int i = 0; i < 4; i++)
            System.out.println(random.nextInt(11));
    }

    void even(int n) {
        System.out.println("even");
        for (int i = 1; i < n; i += 2)
            System.out.println(i);
    }

    void powers(int n) {
        System.out.println("powers");
        for (int i = 1; i <= n; i++)
            System.out.println((int) Math.pow(2, i));
    }

    void infLoop() {
        System.out.println("Inf_loop");
        Scanner sc = new Scanner(System.in);
        String inp = null;
        /*while (true){
            System.out.println("\"Are we there yet?\"");
            inp = sc.nextLine();
            if (inp.equals("Yes")) {
                System.out.println("Good!");
                break;
            }
        }*/
        do {
            System.out.println("\"Are we there yet?\"");
        } while (!sc.nextLine().equals("Yes"));
        System.out.println("Good!");
    }

    void triangle() {
        System.out.println("triangle");
        String star = "*";
        // Avoided a loop
        for (int i = 1; i <= 5; i++)
            System.out.println(star.repeat(i));
    }

    void tableSquare() {
        System.out.println("tableSquare");
        for (int i = 1; i < 5; i++) {
            for (int j = 1; j < 5; j++)
                System.out.print("|" + i * j + "\t");
            System.out.println("|");
        }
    }

    void tableSquares(int n) {
        System.out.println("tableSquare");
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++)
                System.out.print("|" + i * j + "\t");
            System.out.println("|");
        }
    }


    NNLoops() {
        oneToTen();
        oddNumbers();
        squares();
        random4();
        even(20);
        powers(8);
        infLoop();
        triangle();
        tableSquare();
        tableSquares(6);
    }

    public static void main(String[] args) {
        new NNLoops();
    }
}

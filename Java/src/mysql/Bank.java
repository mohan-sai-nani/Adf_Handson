package mysql;

import java.util.Scanner;

public class Bank {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int option;
        boolean flag = true;
        while (flag) {
            System.out.println("""
                    Select your operation:
                    1. Create Account
                    2. Transaction
                    3. Exit""");
            option = sc.nextInt();
            switch (option) {
                case 1 -> new CreateAccount();
                case 2 -> new Transactions();
                case 3 -> flag = false;
                default -> System.out.println("Invalid Input please try again");
            }
        }
        System.out.println("Thank You");
    }
}

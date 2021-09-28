package mysql;

import java.util.Objects;
import java.util.Scanner;
import java.sql.*;

public class CreateAccount {
    Scanner sc = new Scanner(System.in);

    private long get_user_details() {
        long account_number = 123;
        System.out.println("Enter your name:");
        String name = sc.nextLine();
        System.out.println("Enter you Aadhar Number:");
        long aadhar = sc.nextLong();
        sc.nextLine();
        System.out.println("Enter your mobile number:");
        long mobile = sc.nextLong();
        sc.nextLine();
        System.out.println("Enter the Balance:");
        long balance = sc.nextLong();
        sc.nextLine();
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/java_handson?characterEncoding=latin1", "java", "java143");
            String query = "insert into accounts(aadharnumber, cust_name, mobile, balance) values (?,?,?,?)";
            PreparedStatement preparedStmt = con.prepareStatement(query);
            preparedStmt.setLong(1, aadhar);
            preparedStmt.setString(2, name);
            preparedStmt.setLong(3, mobile);
            preparedStmt.setLong(4, balance);
            preparedStmt.execute();
            query = "Select accountnumber from accounts where mobile = ?";
            preparedStmt = con.prepareStatement(query);
            preparedStmt.setLong(1, mobile);
            ResultSet rs = preparedStmt.executeQuery();
            if (rs.next())
                account_number = rs.getLong(1);
            con.close();
        } catch (Exception e) {
            System.out.println(e);
        }
        return account_number;
    }

    private void get_account_details(Long account_number) {
        System.out.println("Select Account Type: 1. Savings, 2. Current");
        int x = sc.nextInt();
        sc.nextLine();
        String account_type = (x == 1) ? "Savings" : "Current";
        System.out.println("Select add-ons:");
        System.out.println("Zero Balance Account (Yes / No)");
        String a = sc.nextLine();
        boolean Zero_bal = Objects.equals(a, "Yes");
        System.out.println("Over Draft Account (Yes / No)");
        a = sc.nextLine();
        boolean OverDraft = Objects.equals(a, "Yes");
        System.out.println("Salary Account (Yes / No)");
        a = sc.nextLine();
        boolean Salary = Objects.equals(a, "Yes");
        System.out.println("Golden Reward Points Account(Yes / No)");
        a = sc.nextLine();
        boolean Gold = Objects.equals(a, "Yes");
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/java_handson?characterEncoding=latin1", "java", "java143");
            String query = "insert into products values(?, ?, ?, ?, ?, ?)";
            PreparedStatement preparedStmt = con.prepareStatement(query);
            preparedStmt.setLong(1, account_number);
            preparedStmt.setString(2, account_type);
            preparedStmt.setBoolean(3, Zero_bal);
            preparedStmt.setBoolean(4, OverDraft);
            preparedStmt.setBoolean(5, Salary);
            preparedStmt.setBoolean(6, Gold);
            preparedStmt.execute();
            con.close();
            System.out.println("Account created Successfully, Account_Number: " + account_number);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public CreateAccount() {
        long account_number = get_user_details();
        if (account_number != 123)
            get_account_details(account_number);
    }
}

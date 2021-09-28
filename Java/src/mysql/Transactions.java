package mysql;

import java.util.Scanner;
import java.sql.*;

public class Transactions {
    Scanner sc = new Scanner(System.in);

    protected String with_drawl() {
        String status = "Failed";
        long balance = 0;
        System.out.println("Enter your Account Number:");
        long acc_num = sc.nextLong();
        sc.nextLine();
        System.out.println("Enter Amount:");
        long amount = sc.nextLong();
        sc.nextLine();
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/java_handson?characterEncoding=latin1", "java", "java143");
            String query = "select balance from accounts where accountnumber=?";
            PreparedStatement preparedStmt = con.prepareStatement(query);
            preparedStmt.setLong(1, acc_num);
            ResultSet rs = preparedStmt.executeQuery();
            if (rs.next())
                balance = rs.getLong(1);
            if (balance < amount)
                status = "Insufficient funds";
            else {
                balance -= amount;
                query = "Update accounts set balance = ? where accountnumber = ?";
                preparedStmt = con.prepareStatement(query);
                preparedStmt.setLong(1, balance);
                preparedStmt.setLong(2, acc_num);
                preparedStmt.execute();
                status = "Success";
                query = "Insert into transactions(" +
                        "tran_status, deposit, " +
                        "withdrawal, balance, accountnumber) " +
                        "values(?, ?, ?, ?, ?)";
                preparedStmt = con.prepareStatement(query);
                preparedStmt.setString(1, status);
                preparedStmt.setLong(2, 0);
                preparedStmt.setLong(3, amount);
                preparedStmt.setLong(4, balance);
                preparedStmt.setLong(5, acc_num);
                preparedStmt.execute();
                System.out.println("Balance: " + balance);
            }
            con.close();
        } catch (Exception e) {
            System.out.println(e);
        }
        return status;
    }

    protected String deposit() {
        String status = "Failed";
        long balance = 0;
        System.out.println("Enter your Account Number:");
        long acc_num = sc.nextLong();
        sc.nextLine();
        System.out.println("Enter Amount:");
        long amount = sc.nextLong();
        sc.nextLine();
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/java_handson?characterEncoding=latin1", "java", "java143");
            String query = "select balance from accounts where accountnumber=?";
            PreparedStatement preparedStmt = con.prepareStatement(query);
            preparedStmt.setLong(1, acc_num);
            ResultSet rs = preparedStmt.executeQuery();
            if (rs.next())
                balance = rs.getLong(1);
            balance += amount;
            query = "Update accounts set balance = ? where accountnumber = ?";
            preparedStmt = con.prepareStatement(query);
            preparedStmt.setLong(1, balance);
            preparedStmt.setLong(2, acc_num);
            preparedStmt.execute();
            status = "Success";
            query = "Insert into transactions(" +
                    "tran_status, deposit, " +
                    "withdrawal, balance, accountnumber) " +
                    "values(?, ?, ?, ?, ?)";
            preparedStmt = con.prepareStatement(query);
            preparedStmt.setString(1, status);
            preparedStmt.setLong(2, amount);
            preparedStmt.setLong(3, 0);
            preparedStmt.setLong(4, balance);
            preparedStmt.setLong(5, acc_num);
            preparedStmt.execute();
            System.out.println("Balance: " + balance);
            con.close();
        } catch (Exception e) {
            System.out.println(e);
        }
        return status;
    }

    public Transactions() {
        System.out.println("Select Transaction Type:\n1. Deposit\n2. With Drawl");
        int opt = sc.nextInt();
        sc.nextLine();
        String status;
        if (opt == 1) {
            status = deposit();
            System.out.println(status);
        } else if (opt == 2) {
            status = with_drawl();
            System.out.println(status);
        } else
            System.out.println("Invalid Input");
    }
}

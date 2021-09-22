package stringsArraysCollections;

import java.util.Arrays;

public class stringsArraysCollections {
    void printArray(String[][] grid){
        for (String[] strings : grid) {
            System.out.print(" | ");
            for (String string : strings) {
                System.out.print(string + " | ");
            }
            System.out.println();
        }
    }

    void ticTacToe(){
        String [][] grid = new String[3][3];
        for (String[] strings : grid) {
            Arrays.fill(strings, "X");
        }
        printArray(grid);
    }

    void chess(){
        String [][] grid = new String[8][8];
        boolean key = false;
        for (int i = 0; i < grid.length; i++){
            key = !key;
            for (int j = 0; j < grid[i].length; j++){
                grid[i][j] = key ? "X" : "O";
                key = !key;
            }
        }
        printArray(grid);
    }

    public static String digitsToWords(String inp){
        String words = "";
        String [] digits = {"Oh", "One", "Two", "Three",
                            "Four", "Five","Six","Seven",
                            "Eight", "Nine"};
        for (int i = 0; i < inp.length(); i++){
            int num = Integer.parseInt(inp.substring(i, i + 1));
            words += digits[num] + " ";
        }
        return words;
    }

    stringsArraysCollections(){
        //ticTacToe();
        //chess();
        //System.out.println(digitsToWords("7036557972"));

    }

    public static void main(String[] args) {
        new stringsArraysCollections();
    }
}

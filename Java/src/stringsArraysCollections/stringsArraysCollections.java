package stringsArraysCollections;

import java.util.Arrays;

public class stringsArraysCollections {
    public static String [] morse_code = {
            ".-", "-...", "-.-.", "-..", ".", "..-.",
            "--.", "....", "..", ".---", "-.-", ".-..",
            "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--..", "/"
    };
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

    public static String timeToWords(String s){
        String time;
        String [] input = s.split(":");
        String [] times = {"o'clock", "one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thirteen",
                "fourteen", "quarter", "sixteen",
                "seventeen", "eighteen", "nineteen",
                "twenty", "twenty one", "twenty two",
                "twenty three", "twenty four", "twenty five",
                "twenty six", "twenty seven", "twenty eight",
                "twenty nine","half past"
        };
        int hours = Integer.parseInt(input[0]);
        int minutes = Integer.parseInt(input[1]);
        String sayMinutes = minutes % 5 != 0 ? "minutes" : ":";
        if (hours == 12 && minutes > 30)
            hours = 1;
        if (minutes == 0)
            time = times[hours] + " o'clock";
        else if (minutes == 15)
            time = "Quarter past " + times[hours];
        else if (minutes == 45)
            time = "Quarter to " + times[hours];
        else if (minutes > 30)
            time = times[60 - minutes] + sayMinutes + " to " + times[hours];
        else
            time = times[minutes] + sayMinutes + " past " + times[hours];
        return time;
    }

    public static String morse(String inp){
        inp = inp.toLowerCase();
        String code = "";
        for (int i = 0; i < inp.length(); i++){
            int num = inp.charAt(i) == ' ' ? 26 : inp.charAt(i) - 97;
            code += morse_code[num] + " ";
        }
        return code;
    }

    public static String deMorse(String inp){
        inp = inp.toLowerCase();
        String text = "";
        String [] letters = inp.split("\\s+");
        for (String s : letters) {
            String letter = s.trim();
            if (letter.equals("/"))
                text += " ";
            else {
                for (int j = 0; j < morse_code.length; j++) {
                    if (letter.equals(morse_code[j])) {
                        char c = (char) (j + 97);
                        text += Character.toString(c);
                    }
                }
            }
        }
        return text;
    }

    stringsArraysCollections(){

        ticTacToe();
        chess();
        System.out.println(digitsToWords("7036557972"));
        System.out.println(timeToWords("12:00"));
        System.out.println(morse("I never saw a purple cow"));
        System.out.println(deMorse(".. / -. . ...- . .-. / ... .- .-- / .- / .--. ..- .-. .--. .-.. . / -.-. --- .--"));
    }

    public static void main(String[] args) {
        new stringsArraysCollections();
    }
}

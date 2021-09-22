package NNArray;
import java.util.Arrays;

public class NNArray {
    void printArray(String[] inp){
        for (String str: inp)
            System.out.println(str);
    }

    public static String lastElement(String[] inp){
        return (inp[inp.length - 1]);
    }

    public static String lastButOne(String[] inp){
        return (inp[inp.length - 2]);
    }

    public static String[] reverse(String[] inp){
        StringBuilder reverse = new StringBuilder();
        for (int i = inp.length; i > 0; i--)
            reverse.append(inp[i - 1]).append(" ");
        inp = reverse.toString().split(" ");
        return inp;
    }

    public static Boolean isPalindrome(String[] inp){
        String[] rev = reverse(inp);
        return Arrays.equals(inp, rev);
    }

    void compress(int[] inp){
        System.out.println(inp[0]);
        for (int i = 1; i < inp.length; i++)
            if (inp[i] != inp[i - 1])
                System.out.println(inp[i]);
    }

    void pack(char[] inp){
        String s = Character.toString(inp[0]);
        for (int i = 1; i < inp.length; i++)
            if (inp[i] != inp[i - 1]) {
                System.out.print(s + ", ");
                s = Character.toString(inp[i]);
            }
            else
                s += inp[i];
        System.out.println(s);
    }

    NNArray(){
        String[] breakfast = {"Sausage", "Eggs", "Beans", "Bacon", "Tomatoes", "Mushrooms"};
        String[] palindromic = {"Sausage", "Eggs", "Beans", "Beans", "Eggs", "Sausage"};
        int [] numbers = {1,1,3,3,3,2,2,2,1,1,1,1,4,4,4,4};
        char [] letters = {'a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e'};
        printArray(breakfast);
        System.out.println(lastElement(breakfast));
        System.out.println(lastButOne(breakfast));
        printArray(reverse(breakfast));
        System.out.println(isPalindrome(palindromic));
        System.out.println(isPalindrome(breakfast));
        compress(numbers);
        pack(letters);
    }

    public static void main(String[] args) {
        new NNArray();
    }
}

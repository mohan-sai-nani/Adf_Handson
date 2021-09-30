package Functional;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Arrays {

    public boolean isPalindromeUsingIntStream(String s) {
        String temp  = s.replaceAll("\\s+", "").toLowerCase();
        return IntStream.range(0, temp.length() / 2)
                .noneMatch(i -> temp.charAt(i) != temp.charAt(temp.length() - i - 1));
    }
    public boolean isPalindromeUsingStringBuilder(String s){
        String reversedString = new StringBuilder(s).reverse().toString();
        return s.equals(reversedString);
    }

    public static void main(String[] args) {
        List<String> breakfast = List.of("Sausage", "Eggs", "Beans", "Bacon", "Tomatoes", "Mushrooms");
        List<String> palindromic = List.of("MOM", "Eggs", "computer", "radar", "Eggs", "abcba");
        List<Integer> numbers = List.of(1,1,3,3,3,2,2,2,1,1,1,1,4,4,4,4);
        List<Character> letters = List.of('a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e');
        breakfast.stream()
                .forEach(System.out::println);
        System.out.println(breakfast.stream()
                .reduce((first, second) -> second));
        System.out.println(breakfast.stream()
                .skip(breakfast.size() -2)
                .findFirst());
        new LinkedList<>(breakfast)
                .descendingIterator()
                .forEachRemaining(System.out::println);
        breakfast.stream()
                .collect(Collectors.toCollection(LinkedList::new))
                .descendingIterator();
        palindromic.stream()
                .filter(s -> Objects.equals(s, new StringBuilder(s).reverse().toString()))
                .forEach(System.out::println);
    }
}

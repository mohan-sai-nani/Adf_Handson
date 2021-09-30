package Functional;

import java.util.List;

public class StreamLambda {
    public static void main(String[] args) {
        List <Integer> numbers = List.of(1,2,3,4,5,6,7,8,9,10);
        System.out.println(numbers.stream()
                .filter(number -> number%2 == 0)
                .map(number -> number * number)
                .reduce(0, Integer::sum));
    }
}

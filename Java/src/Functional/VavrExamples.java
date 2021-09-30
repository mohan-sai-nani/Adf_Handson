package Functional;

import static io.vavr.API.$;
import static io.vavr.API.Match;
import static io.vavr.API.Case;

public class VavrExamples {
    public static void main(String[] args) {
        int input = 2;
        String output = Match(input).of(
                Case($(1), "one"),
                Case($(2), "two"),
                Case($(3), "three"),
                Case($(), "?"));
        System.out.println(output);
    }
}

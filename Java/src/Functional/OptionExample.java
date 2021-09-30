package Functional;


import io.vavr.control.Option;

public class OptionExample {
    public static void main(String[] args) {
        System.out.println(Option.of(null));
        Option<String> value = Option.some("NaNi");
        Option<String> value1 = Option.none();
        System.out.println(value.get());
        System.out.println(value.map(a->a).getOrElse("Default"));
        System.out.println(value1.map(a->a).getOrElse("Default"));
    }
}

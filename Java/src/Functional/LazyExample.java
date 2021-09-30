package Functional;

import io.vavr.Lazy;

public class LazyExample {
    public static void main(String[] args) {
        Lazy<Double> name = Lazy.of(Math::random);
        System.out.println(name.isEvaluated());
        System.out.println(name.get());
        System.out.println(name.isEvaluated());
        System.out.println(name.get());
    }
}

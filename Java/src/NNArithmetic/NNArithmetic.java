package NNArithmetic;

public class NNArithmetic {
    public static boolean isPrime(int n) {
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;
        if (n % 2 == 0 || n % 3 == 0)
            return false;
        for (int i = 5; i * i <= n; i += 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        return true;
    }

    public static int gcd(int a, int b) {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }

    public static boolean isCoPrime(int a, int b) {
        return gcd(a, b) == 1;
    }

    public static int phi(int n) {
        float result = n;
        for (int i = 2; i * i <= n; ++i) {
            if (n % i == 0) {
                while (n % i == 0)
                    n /= i;
                result *= (1.0 - (1.0 / (float) i));
            }
        }
        if (n > 1)
            result *= (1.0 - (1.0 / (float) n));
        return (int) result;
    }

    void printPrimeFactors(int n) {
        while (n % 2 == 0) {
            System.out.println(2 + " ");
            n /= 2;
        }
        for (int i = 3; i * i <= n; i += 2)
            while (n % i == 0) {
                System.out.print(i + " ");
                n /= i;
            }
        if (n > 2)
            System.out.println(n);
    }

    void printPrimesInRange(int a, int b) {
        if (a == 1) {
            System.out.print(a + " ");
            a++;
            if (b >= 2) {
                System.out.print(a + " ");
                a++;
            }
        }
        if (a == 2)
            System.out.print(a + " ");
        if (a % 2 == 0)
            a++;
        for (int i = a; i <= b; i = i + 2) {
            int flag = 1;
            for (int j = 2; j * j <= i; ++j) {
                if (i % j == 0) {
                    flag = 0;
                    break;
                }
            }
            if (flag == 1)
                System.out.print(i + " ");
        }
    }

    void printGoldBachPair(int[] pair) {
        System.out.println(pair[0] + " + " + pair[1] + " = " + pair[2]);
    }

    public static int[] goldBachPair(int n) {
        int count = 2;
        int[] pair = new int[3];
        boolean foundPair = false;
        while (!foundPair && count <= n / 2) {
            if (isPrime(count) && isPrime(n - count)) {
                foundPair = true;
                pair[0] = count;
                pair[1] = (n - count);
            }
            count++;
        }
        pair[2] = n;
        return pair;
    }

    void printGoldBachList(int a, int b) {
        int[] pair;
        if (a % 2 != 0)
            a++;
        for (int i = a; i <= b; i += 2) {
            pair = goldBachPair(i);
            printGoldBachPair(pair);
        }
    }

    void printGoldBachList(int a, int b, int limit) {
        int[] pair;
        if (a % 2 != 0)
            a++;
        for (int i = a; i <= b; i += 2) {
            pair = goldBachPair(i);
            if (pair[0] > limit && pair[1] > limit)
                printGoldBachPair(pair);
        }
    }


    NNArithmetic() {
        int n = 1856;
        System.out.println(isPrime(71));
        System.out.println();
        System.out.println(gcd(1071, 462));
        System.out.println();
        System.out.println(isCoPrime(35, 64));
        System.out.println();
        System.out.println(phi(10));
        System.out.println();
        printPrimeFactors(315);
        System.out.println();
        printPrimesInRange(10, 20);
        System.out.println();
        int[] pair = goldBachPair(1856);
        printGoldBachPair(pair);
        System.out.println();
        printGoldBachList(9, 20);
        System.out.println();
        printGoldBachList(1, 2000, 50);
    }

    public static void main(String[] args) {
        new NNArithmetic();
    }
}

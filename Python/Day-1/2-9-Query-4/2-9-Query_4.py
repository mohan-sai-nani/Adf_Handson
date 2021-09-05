def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


if __name__ == '__main__':
    try:
        print("Enter the values separated by Space: ")
        li = list(map(int, input().split()))
        num1 = li[0]
        num2 = li[1]
        gcd = find_gcd(num1, num2)
        for i in range(2, len(li)):
            gcd = find_gcd(gcd, li[i])
        print("GCD of given numbers is: ", gcd)
    except():
        print('An Error Occurred')

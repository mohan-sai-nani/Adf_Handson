# Decimal to Binary
# Octal to Hexadecimal

if __name__ == '__main__':
    try:
        while 1:
            print("1. Decimal to Binary \n2. Octal to Hexadecimal \n3. Exit")
            print("Choose your option:")
            option = int(input())
            if option == 1:
                print("Enter Binary Number: ")
                n = int(input())
                print("Binary: ", bin(n))
            elif option == 2:
                print("Enter Octal Number: ")
                n = int(input(), 8)
                print("Hexadecimal: ", hex(n))
            elif option == 3:
                break
            else:
                print("Invalid Input Try again")
    except():
        print("An Error Occurred")

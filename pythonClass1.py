num = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print("\n===INSTRUCTIONS===\nPress 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division\nPress 5 for remainder\n")

opt = int(input("Enter operation: "))

if opt == 1:
    print("Your sum is" , (num + num2))
elif opt == 2:
    print("Your difference is" , (num - num2))
elif opt == 3:
    print("Your product is" , (num * num2))
elif opt == 4:
    print("Your quotient is" , (num // num2))
elif opt == 5:
    print("Your remainder is" , (num % num2))
else:
    print('Invalid Input')
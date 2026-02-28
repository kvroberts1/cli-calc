user_input = 0
number1 = 0
number2 = 0

print("Select Operation desired.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try:

    user_input = float(input("Select Number 1 - 4: "))

    if user_input == 1 :
            number1 = float(input("You choose addition. What is the first number you would like to add: "))
            number2 = float(input(f'{number1} + X. What does X equal? '))
            print(number1 + number2)
    elif user_input == 2 :
            number1 = float(input("You choose subtraction. What is the first number you would like to subtract: "))
            number2 = float(input(f'{number1} - X. What does X equal? '))
            print(number1 - number2)
    elif user_input == 3 :
            number1 = float(input("You choose multiplication. What is the first number you would like to multiply: "))
            number2 = float(input(f'{number1} * X. What does X equal? '))
            print(number1 * number2)
    elif user_input == 4 :
            number1 = float(input("You choose division. What is the first number you would like to divide: "))
            number2 = float(input(f'{number1} / X. What does X equal? '))
            if number2 == 0 :
                print("0")
            else:
                print(number1 / number2)
    else:
            print("What is happening? You screwed that up.")

except:
    print("Only INTs allowed")
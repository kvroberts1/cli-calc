user_input = 0
number1 = 0
number2 = 0
status_off = 0

def add(number1, number2):
        return(number1 + number2)

def sub(number1, number2):
        return(number1 - number2)

def multi(number1 , number2):
        return(number1 * number2)

def div(number1, number2):
        if number2 == 0 :
                return("0")
        else:
                return(number1 / number2)

while status_off == 0:

        print("Select Operation desired.")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:

                user_input = float(input("Select Number 1 - 5: "))
                number1 = float(input("Choose your first number: "))
                number2 = float(input("Choose your second number: "))

                if user_input == 1 :
                        print(add(number1, number2))
                elif user_input == 2 :
                        print(sub(number1, number2))
                elif user_input == 3 :
                        print(multi(number1, number2))
                elif user_input == 4 :
                        print(div(number1, number2))
                elif user_input == 5 :
                        status_off = 1

        except:
                print("Only INTs allowed")
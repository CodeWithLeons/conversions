# Temperature Converter
# This temperature Converter Python Script does a 2 way conversion between Celsius and Fahrenheit and Kelvin. 

def input_temp(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a numerical value")


def msg():
    print("1. Celsius ⇋ Fahrenheit \n2. Celsius ⇋ Kelvin \n3. Fahrenheit ⇋ Kelvin")


while True:

    msg()
    while True:

        tk = int(input("select conversion to be performed \n>>>"))
        if tk not in [1, 2, 3]:
            print("Select a number from 1 - 3")
        else:
            break

    if tk == 1:
        print("1. ℃ ⇋ F \n2. F ⇋ ℃")
        while True:
            check_select = int(input("select conversion to be performed \n>>>"))
            if check_select not in [1, 2]:
                print("select 1 or 2")
            else:
                break
        if check_select == 1:
            celsius = input_temp("Temperature in Celsius: ")
            fahrenheit = (celsius * 9/5) + 32
            fahrenheit = round(fahrenheit, 1)
            print(celsius, "℃ =", fahrenheit, "F")
        elif check_select == 2:
            fahrenheit = input_temp("Temperature in Fahrenheit: ")
            celsius = (fahrenheit - 32) * 5/9
            celsius = round(celsius, 1)
            print(fahrenheit, "F =", celsius, "℃")

    elif tk == 2:
        print("1. ℃ ⇋ K \n2. K ⇋ ℃")
        while True:
            check_select = int(input("select conversion to be performed \n>>>"))
            if check_select not in [1, 2]:
                print("select 1 or 2")
            else:
                break
        if check_select == 1:
            celsius = input_temp("Temperature in Celsius: ")
            kelvin = celsius + 273.15
            kelvin = round(kelvin, 1)
            print(celsius, "℃ =", kelvin, "K")
        elif check_select == 2:
            kelvin = input_temp("Temperature in Kelvin: ")
            celsius = kelvin - 273.15
            celsius = round(celsius, 1)
            print(kelvin, "K =", celsius, "℃")

    elif tk == 3:
        print("1. F ⇋ K \n2. K ⇋ F")
        while True:
            check_select = int(input("select conversion to be performed \n>>>"))
            if check_select not in [1, 2]:
                print("select 1 or 2")
            else:
                break
        if check_select == 1:
            fahrenheit = input_temp("Temperature in Fahrenheit: ")
            celsius = (fahrenheit - 32) * 5 / 9
            kelvin = celsius + 273.15
            kelvin = round(kelvin, 1)
            print(fahrenheit, "F =", kelvin, "K")
        elif check_select == 2:
            kelvin = input_temp("Temperature in Kelvin: ")
            celsius = kelvin - 273.15
            fahrenheit = (celsius * 9 / 5) + 32
            fahrenheit = round(fahrenheit, 1)
            print(kelvin, "K =", fahrenheit, "F")


    print("\n")


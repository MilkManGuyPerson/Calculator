print("Calculator")
print(" ")
mathtype = input("Choose math type *, /, +, -. ")
print(" ")
number = input("How many numbers whould you like to calculate? (2-5) ")
print(" ")
if mathtype == "/" and number == "2":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    answer = first_number / second_number
    print(answer)
elif mathtype == "+" and number == "2":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    answer = first_number + second_number
    print(answer)
elif mathtype == "-" and number == "2":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    answer = first_number - second_number
    print(answer)
elif mathtype == "*" and number == "2":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    answer = first_number * second_number
    print(answer)
elif mathtype == "/" and number == "3":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: ")) 
    answer = first_number / second_number / third_number
    print(answer)
elif mathtype == "*" and number == "3":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: ")) 
    answer = first_number * second_number * third_number
    print(answer)
elif mathtype == "+" and number == "3":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: ")) 
    answer = first_number + second_number + third_number
    print(answer)
elif mathtype == "-" and number == "3":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: ")) 
    answer = first_number - second_number - third_number
    print(answer)
elif mathtype == "-" and number == "4":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: "))
    fourth_number = float(input("Enter fourth number: ")) 
    answer = first_number - second_number - third_number - fourth_number
    print(answer)
elif mathtype == "+" and number == "4":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: "))
    fourth_number = float(input("Enter fourth number: ")) 
    answer = first_number + second_number + third_number + fourth_number
    print(answer)
elif mathtype == "*" and number == "4":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: "))
    fourth_number = float(input("Enter fourth number: ")) 
    answer = first_number * second_number * third_number * fourth_number
    print(answer)
elif mathtype == "/" and number == "4":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: "))
    fourth_number = float(input("Enter fourth number: ")) 
    answer = first_number / second_number / third_number / fourth_number
    print(answer)
elif mathtype == "/" and number == "5":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: "))
    fourth_number = float(input("Enter fourth number: "))
    fifth_number = float(input("Enter fifth number: "))
    answer = first_number / second_number / third_number / fourth_number / fifth_number
    print(answer)
elif mathtype == "*" and number == "5":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: "))
    fourth_number = float(input("Enter fourth number: "))
    fifth_number = float(input("Enter fifth number: "))
    answer = first_number * second_number * third_number * fourth_number * fifth_number
    print(answer)
elif mathtype == "+" and number == "5":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: "))
    fourth_number = float(input("Enter fourth number: "))
    fifth_number = float(input("Enter fifth number: "))
    answer = first_number + second_number + third_number + fourth_number + fifth_number
    print(answer)
elif mathtype == "-" and number == "5":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    third_number = float(input("Enter third number: "))
    fourth_number = float(input("Enter fourth number: "))
    fifth_number = float(input("Enter fifth number: "))
    answer = first_number - second_number - third_number - fourth_number - fifth_number
    print(answer)
elif number == "1":
    print('No.')
else:
    print("That is not a valid math type and/or number.")
    print(" ")
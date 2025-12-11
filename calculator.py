while True :

    print("\n--- Simple Calculator ---")

      # get numbers with error handling

    try: 
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only")
        continue


        # choose operation

    operation = input("Enter the operation (+, - , *, /) : ")

        # logic calculation

    if operation == '+' :
        result = num1 + num2
    elif operation == '-' :
        result = num1 - num2
    elif operation == '*' :
        result = num1 * num2
    elif operation == '/' :
        if num2 == 0 :
            print("Error : cannot divide by 0")
            result = None
        else :
             result = num1 / num2
    else :
        print("Invalid operation")
        result = None

        # show result

        if result is not None:
         print("The result is : ", result)
    
        # loop control
    
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
      print("Goodbye!")
      break


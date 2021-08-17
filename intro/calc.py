"""
System: Simple calculator
Author: Robert Tulanko
functionality:
    - Sum
    - Subtract
    - Multiply
    - Divide
"""

# imports need placed here
from display import print_menu

# Then global variables
"""
    division
    if the user tries to divide by zero:
        show an error "Crashed the cosmos"
        result to 0

"""


# then functions




# and then plain instructions
opt = ""
while(opt != "x"):
    print_menu()
    opt = input("Choose an option: ")
    if(opt == "x"):
        break

    try: 
            num1 = float(input("Provide num1:"))
            num2 = float(input("Provide num2:"))
    except:
        print("Invalid input, try again")
        continue 

    if(opt == "1"):
        print(f"The result is: {num1 + num2}")

    elif(opt == "2"):
        print(f"The result is: {num1 - num2}")

    elif(opt == "3"):
        print(f"The result is: {num1 * num2}")

    elif(opt == "4"):
        if(num2 == 0):
            print("Error: COSMOS AT STAKE")
        else:
            print(f"The result is: {num1 / num2}")

    elif(opt == "5"):
        for i in range(3):
            print("Your text here")
        else: 
            print(f"Your message: ")*3
    
    input("Press Enter to continue my guy...")

print("Good bye")
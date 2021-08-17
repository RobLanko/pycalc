print("Hello from Python")

# is a single line comment


# variables and variable types
name = "Robbie"
print(name)

age = 98
total = 19.99
found = True


print(age)
print(total)
print(found)
print(name + name) #this is a string concatenation
print(age + 1) #sum
print(name + str(age))

if(age < 100):
    print("You are still young!")
    print("Another line inside of the if")
elif (age ==100):
    print("You're almost there!")
else:
    print("Sorry, you ar old af")

print("Line outside of the if")



# definition of a funtction
def test():
    print("Hello, I'm just a test bro")




test() # call or execute a function
test()
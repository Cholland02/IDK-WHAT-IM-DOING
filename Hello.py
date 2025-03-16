import math

print("Hello!")
name=input("What is your name?")
print("Hello, " + name + "!")
age=input("How old are you?")
print("Wow, " + name  + ", you are " + age + " years old!")
print("I am a computer program, so I dont have an age, but if I did, I would be " + str(2023 - 2020) + " years old!")
print( "Did you know that I can do math? I can add, subtract, multiply, and divide!")
while True:
    equation = input("Enter a math equation (or type 'quit' to exit): ")
    if equation.lower() == 'quit':
        break
    try:
        result = eval(equation)
        print("The result of the equation is: " + str(result))
    except Exception as e:
        print("There was an error with your equation: " + str(e))

print("You're awesome! Thanks for using the program.")
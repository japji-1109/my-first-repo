#TODO: To add something in the middle of a string:-
# print("Hello", "World", sep="!")

#TODO: To add something in the end of the something we use end
# print("Hello Word", end="!")

#TODO: To save the text in a file by overwrting.
# print("Hello World!!", file = open("main.js", "w"))


# name = input("What's your name?")
# age = input("What is your age?")

# print(f"My name is {name}, and age is {age}")

#TODO: VARIABLES:- THEY ARE NOT MUTABLE AS THEY ASSIGNED DIFFERENT IDS BY THE MACHINE
# name_of_variable = 10
# print(name_of_variable, id(name_of_variable))
# name_of_variable = 15
# print(name_of_variable, id(name_of_variable))

# TODO: IDENTIFYING THE IDS AND ALSO VARIABLE ARE IMMUTABLE
# x = 7
# y = x
# print(y+1);print(x)
# print(id(x), id(y))

# fname = "aditya"
# print(fname[0])

#IF STATEMENTS - CONDITIONAL STATEMENTS


# if username == "abc":
#     if password == "password":
#         print("You are authenticated.")

#         # OR

# if username == "abc" and passowrd="password":
#     print("You are authenticated!!")

    # OR
# a = id(username)
# b = id(password)

# password = input("Enter your password: ")

# or
# if username == "abc":
#     if password == "password":
#         print("You're authenticated!!")
#     elif password == "xyz":
#         print("You are not authenticatded!!")

# username = "abc"
# password = "password"


# username = input("What is your username?")
# passowrd = input("Enter ur password: ")

# otp = 1234
# limit = 0

# while limit < 3:
#     limit = limit +1
#     if username == "abc" and password == "password":
#         user_input = input("Enter your otp ")
#         if user_input == otp:
#             print("You are logged in")
#         else:
#             print("Wrong OTP")


#Conversion of types:
age = 24
int_to_str = str(age)
print(type(int_to_str))

x= 10
y = 20
print(x==10, y==30)
# Ask user for their name
name = input("what's your name? ")


#Remove whitespace from str 
#and capitalize user's name
name = name.strip()
name = name.title()

#split user's name into first name and last name
first, last = name.split(" ")


# Say hello to user
print("hello, ", end="")
print(f'"{name}"')


# escape quotes
# print(" \"a\" ")

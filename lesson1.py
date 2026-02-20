# Ask user for their name
name = input("what's your name? ")

name = name.strip()
name = name.title()
# Say hello to user
print("hello, ", end="")
print(f'"{name}"')


# escape quotes
# print(" \"a\" ")

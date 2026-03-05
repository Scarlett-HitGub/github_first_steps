# import_as allows us to tight up a large or very use name module
import random as rd

#calls a numbre from a range
number = rd.randint(1, 10)
print(number)

#shuffle a list of participants
participants = (["scarlett", "vicky", "kote"])
rd.shuffle(participants)
for pt in participants:
    print(pt)

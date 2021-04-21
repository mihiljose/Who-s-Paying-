# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

# no_of_ppl = len(names)

# payee = random.randint(0,no_of_ppl-1)

# print(f"{names[payee]} is paying today")

#or
print(f"{random.choice(names)} is paying today")

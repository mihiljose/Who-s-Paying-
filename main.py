# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

no_of_ppl = len(names)


payee = random.randint(0,no_of_ppl)

print(f"{names[payee]} is paying today")


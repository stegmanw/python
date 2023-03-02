
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_len = len(names)
random_name = random.randint(0, random_len - 1)
sucker = names[random_name]
print(sucker + " is going to buy the meal today!")


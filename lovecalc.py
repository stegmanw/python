
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

t = lower_case_name1.count("t") + lower_case_name2.count("t")
r = lower_case_name1.count("r") + lower_case_name2.count("r")
u = lower_case_name1.count("u") + lower_case_name2.count("u")
e = lower_case_name1.count("e") + lower_case_name2.count("e")


l = lower_case_name1.count("l") + lower_case_name2.count("l")
o = lower_case_name1.count("o") + lower_case_name2.count("o")
v = lower_case_name1.count("v") + lower_case_name2.count("v")
e = lower_case_name1.count("e") + lower_case_name2.count("e")

x = t + r + u + e
y = l + o + v + e

x = str(x)
y = str(y)

score_str = (x + y)

if int(score_str) < 10 or int(score_str) > 90:
    print(f"Your score is {score_str}, you go together like coke and mentos.")
elif int(score_str) >= 40 and int(score_str) <= 50:
    print(f"Your score is {score_str}, you are alright together.")
else:
    print(f"Your score is {score_str}")

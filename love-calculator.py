#https://app.codingrooms.com/w/jM821OGRPjHQ
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first_number = 0
second_number = 0
name1_lower = name1.lower()
name2_lower = name2.lower()


for x in 'true':
    first_number += name1_lower.count(x)
    first_number += name2_lower.count(x)
    
for x in 'love':
    second_number += name1_lower.count(x)
    second_number += name2_lower.count(x)

current_score = int(str(first_number) + str(second_number))

if current_score < 10 or current_score > 90:
    print(f"Your score is {current_score}, you go together like coke and mentos.")

elif current_score >= 40 and current_score <= 50:
    print(f"Your score is {current_score}, you are alright together.")

else:
    print(f"Your score is {current_score}.")
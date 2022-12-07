# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
current_bill = 0
if size == 'S':
    current_bill += 15
    if add_pepperoni == 'Y':
        current_bill += 2
elif size == 'M':
    current_bill += 20
    if add_pepperoni == 'Y':
        current_bill += 3
elif size == 'L':
    current_bill += 25
    if add_pepperoni == 'Y':
        current_bill += 3

if extra_cheese == 'Y':
    current_bill += 1
    print(f'Your final bill is: ${current_bill}.')
else:
    print(f'Your final bill is: ${current_bill}.')
#Project using DICTIONARY and CONDITIONAL STATEMENTS
#Define the menu of the restaurant
menu = {
    'Chicken Biryani': 210,
    'Mutton Biryani': 253,
    'Chicken Family Pack': 552,
    'Mutton Family Pack': 576,
    'Special Chicken Biryani': 337,
    'Special Mutton Biryani':351,
    'Supreme Chicken Biryani':784,
    'Supreme Mutton Biryani':819,
    'Egg Biryani':154,
    'Veg Biryani':154,
    'Veg Family Pack':383,
    'Veg Supreme Pack':574,
}

#Greet
print("Welcome to PYTHON Paradise")


print("Chicken Biryani: Rs210\nMutton Biryani: Rs253\nChicken Family Pack: Rs552\nMutton Family Pack: Rs576\nSpecial Chicken Biryani: Rs337\nSpecial Mutton Biryani: Rs351\nSupreme Chicken Biryani: Rs784\nSupreme Mutton Biryani: Rs819\nEgg Biryani: Rs154\nVeg Biryani: Rs154\nVeg Family Pack: Rs383\nVeg Supreme Pack: Rs574\n")

order_total = 0
#210 +154 = 364

item_1=input("Enter the name of item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]#0+154
    print(f"Your item {item_1} has been added to your Order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No):")

if another_order == "Yes":
    item_2 = input("Enter the name of second item:")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of ordered items to pay is {order_total}")

print("Thanks, Visit again!")
# Functions & Operator Activity - Alvert Lin
# Step 1
menu = {"Pizza": 2.99, 
        "Burger": 3.99, 
        "Hot dog": 1.99, 
        "Cheese": 0.59, 
        "Ice cream": 1.49, 
        "Churro": 0.79, 
        "Soda": 0.89}

# Step 2

def total_price(item1, item2):
    if item1 not in menu or item2 not in menu: 
        print("items not in menu")
    else: 
        total_sum = menu[item1] + menu[item2]
        print(f"{item1} + {item2} is a combined total of {total_sum}")
        return total_sum

# Stretch 1 
print(f"\nWhat would you like? \n {menu}")
item1 = input("Enter item1: ")
item2 = input("Enter item2: ")
total_test = total_price(item1, item2)
print(total_test)
#print(f"The total price of Pizza and a Burger is: {total_test}")


























#Other Code/Previous Code below


# Stretch 2 + 3 
#order = input(f"What is your order? Menu: {menu}" ) # Stretch 2
#if order not in menu: 
#    print("Sorry, we don't have that here." ) 
#    order = input("Try again: ") 
#    if order not in menu: 
#        print("Okay last chance")
#        order = input("Try again")
#        if order not in menu: 
#            exit("Okay you don't want anything, get out. ")
        
#order2 = input(f"anything else? ") # Stretch 3
#if order2 not in menu:
#    print("Sorry, we don't have that here." ) 
#    order2 = input("Try again: ") 
#    if order2 not in menu: 
#        print("Okay, you don't want another item, but we'll charge you for cheese")
#        order2 == menu["Cheese"]
     
        

#def total_cost(order, order2): # Stretch 3
#    total_cost2 = menu[order] + menu[order2] 
##    return total_cost2





#if order in menu: # Stretch 2
#    print(f"Okay so your pay for your {order} will be {menu[order]}")
#elif order not in menu:
#    print("Sorry, we don't have that here." )



#if order2 in menu: # Stretch 3
 #   print(f"Your other order, {order2}, will cost you {menu[order2]}") 
#else:
#    print("okay")
#if order and order2 in menu:
#    print(f"So your total pay is {total_pay}")
#else:
#    print(f"So your total payis {menu[order]}")



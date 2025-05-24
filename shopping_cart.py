# Author: Pintu
# Date: 2025-05-23
# Description: This script implements a simple shopping cart system.
# It allows users to add, remove, and view items in their cart.

print("Welcome to the Shopping Cart Program!")



#setting restart variable to yes for first iteration

restart = "yes"

#taking input from user
# name,price,quantity
while restart != "no":
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price of the item: "))
    item_quantity = int(input("Enter the quantity of the item: "))
    #calculating total price
    # and handling exceptions
    try:
        total_price = item_price * item_quantity
     
        if total_price > 100:
            discount = total_price * 0.1
            total_price -= discount
            print(f"\nYou saved ${discount:.2f} with a 10% discount!")
            print(f"Discounted Total: ${total_price:.2f}")

        else:
            print(f"\nNo discount applied. Total price for {item_name} is: ${total_price:.2f}")
         
    except ValueError:
        print("Invalid input. Please enter a valid number for price and quantity.")
        continue
    print("Do you want to add more items to the cart? (yes/no)")
    restart = input("Enter your choice: ").lower()

# Displaying the final cart summary
print('\nFinal Cart Summary:')
print(f"Item: {item_name} | Price: ${item_price:.2f} | Quantity: {item_quantity} | Total: ${total_price:.2f}") 
# Thanking the user
print("Thank you for shopping with us!")

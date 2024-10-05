import os, time, random

menu_items = (
    "Cheeseburger",
    "Grilled Chicken Sandwich",
    "Veggie Burger",
    "Chicken Tenders (4 pcs)",
    "Beef Hotdog",
    "French Fries",
    "Onion Rings",
    "Mozzarella Sticks (6 pcs)",
    "Side Salad",
    "Sweet Potato Fries",
    "Cola (small)",
    "Iced Tea (medium)",
    "Lemonade (large)",
    "Bottled Water",
    "Coffee",
    "Chocolate Chip Cookie",
    "Ice Cream Cone",
    "Brownie",
    "Apple Pie",
    "Milkshake (chocolate/vanilla)"
)

item_price = (
    4.99, 5.99, 4.49, 6.99, 3.99, 2.49,
    2.99, 3.49, 1.49, 1.00, 1.99, 2.99,
    1.99, 1.50, 2.50, 1.75, 2.00, 2.25,
    2.75, 3.00
)



os.system("cls")
splash = open(r"E:\Coding\Python\Restaurant\FastFood-System\Splash.txt", "r")
splash_read = splash.read()
print(splash_read)
splash.close()
time.sleep(2)
os.system("cls")

menu = open(r"E:\Coding\Python\Restaurant\FastFood-System\Menu.txt", "r")
menu_read = menu.read()
print(menu_read)
menu.close()
print("=====================================================")
while True:
    p = int(input("Enter item number (0-19) or -1 to exit: "))
    
    if p == -1:
        os.system("cls")
        break  # Exit the loop if the user enters -1
    elif p < 0 or p >= len(menu_items):
        print("Invalid input. Please enter a number between 0 and 19.")
    else:
        print(f"{menu_items[p]} - ${item_price[p]:.2f}")
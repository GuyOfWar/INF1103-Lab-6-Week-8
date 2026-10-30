import json
import os
from Product import Product
from Inventory import Inventory
prompt = int(0)
inventory = Inventory() #creating inventory object from Inventory class
product1 = Product("P001", "Laptop", 1200.00, 15) #creating product from Product class via init
product2 = Product("P002", "Mouse", 25.50, 40)
product3 = Product("P003", "Keyboard", 45.00, 40)
product4 = Product("P004", "Monitor", 299.99, 10)
newproduct = ()
def title_display(): #print out title
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
def menu_display(): #print out menu
    print("\n------------MENU------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
def load_inventory(): #load json
    global inventory
    if not os.path.exists("inventory.json") or os.path.getsize("inventory.json") == 0: #If file doesn't exist or is empty
        with open("inventory.json", "w") as file: #create empty file and activate Inventory to read from
            json.dump([], file)
        inventory = Inventory()
        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.add_product(product3)
        inventory.add_product(product4)
        save_inventory()
    else:    
        with open("inventory.json", "r") as file: #open and load json
                try:
                    data = json.load(file) #load json file into data variable as dictionary
                    inventory = Inventory() #activate Inventory
                    inventory.load_list(data) #put data from json into Inventory
                except json.JSONDecodeError:
                    inventory = Inventory()  # Fallback if the file is corrupted & activate Inventory to read from
                    inventory.add_product(product1)
                    inventory.add_product(product2)
                    inventory.add_product(product3)
                    inventory.add_product(product4)
                    save_inventory()
    print("\ninventory.json found.")
    print("Inventory loaded successfully.")

def add_product(): #option 2
    print("\nAdd New Product")
    while True: #check for duplicate product id when adding new product
        Pid= input("Product ID: ").capitalize()
        if inventory.product_id_check(Pid): #check if id matches the id in inventory list
            print("Error. Product ID already exists! Choose a different Product ID.")
        else:
            break
    Pname= input("Product Name: ").title()
    while True:
        try: #converts input to float without crashing if it fails by jumping to except block
            Price = float(input("Price: "))
            if Price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            break  # Exit loop if input is valid
        except ValueError: #when input is not numbers
            print("Invalid input! Please enter a valid number.")
    while True:
        try: #converts input to int without crashing if it fails by jumping to except block
            Quantity = int(input("Stock Quantity: "))
            if Quantity < 0:
                print("Stock cannot be negative. Please try again.")
                continue
            break  # Exit loop if input is valid
        except ValueError: #when input is not numbers
            print("Invalid input! Please enter a valid whole number.")
    print("\nProduct added successfully!\n")
    new_product= Product(Pid, Pname, Price, Quantity) #creates new Product
    inventory.add_product(new_product) #add new Product into Inventory

def update_stock(): #option 3
    print("\nUpdate Stock")
    while True: #check if product id is in inventory_list
        ProductID= input("Enter Product ID:").capitalize()
        IDcheck= inventory.product_id_check(ProductID) #gets specific id from Inventory to use
        if IDcheck is not None: 
            print("\nProduct Found:")
            print(f"Name: {IDcheck.name()}")
            print(f"Current Stock: {IDcheck.stock()}")
            break
        else:
            print("Product ID not found. Try again.")
    while True:
            try: #converts input to int without crashing if it fails by jumping to except block
                stock= int(input("\nNew Stock Quantity:"))
                if stock < 0:
                    print("Stock cannot be negative. Please try again.")
                    continue
                break  # Exit loop if input is valid
            except ValueError: #when input is not numbers
                print("Invalid input! Please enter a valid whole number.")    
    IDcheck.update_stock(stock) #uses id from Inventory to update stock in Inventory
    print("\nStock updated successfully!")

def save_inventory(): #option 5 & 6, save to json and dump the dictionary into it
    with open('inventory.json', 'w') as file:
        json.dump(inventory.to_list(), file, indent=4)
#main
title_display()
load_inventory()
menu_display()
while True: 
    prompt= input("\nEnter Option:")
    if prompt== "1":
       inventory.display_all()
    elif prompt== "2":
        add_product() #now uses Product & Inventory class inside the function
    elif prompt== "3":
        update_stock() #now uses Product & Inventory class inside the function
    elif prompt== "4":
        inventory.search_product()
    elif prompt== "5":
        print("\nSaving inventory...")
        save_inventory()
        print("Inventory saved successfully to inventory.json.")
    elif prompt== "6":
        print("\nSaving Inventory before exit...")
        save_inventory()
        print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break #exits program
    else:
        print("Invalid Option. Please key in the numbers 1-6.")

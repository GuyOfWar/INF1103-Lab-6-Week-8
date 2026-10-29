from Product import Product
class Inventory:
    def __init__(self):
         self.__inventory_list = []
         
    def display_all(self):
        print("Current Inventory")
        print("-------------------------------------")
        for product in self.__inventory_list: #loop and print
            product.display_information()
        print("-------------------------------------")

    def search_product(self, product_id):
        for product in self.__inventory_list:
            if product.product_id == product_id: #check if id matches the id in inventory list
                print("\nProduct Found")
                print("-------------------------------------")
                print(f"ID:  {product.product_id()}")
                print(f"Name:  {product.name()}")
                print(f"Price: ${product.price():.2f}")
                print(f"Stock: {product.stock()}")
                print("-------------------------------------")
            else:
                print("\nProduct not found.")

    def add_product(self, product):
        self.__inventory_list.append(product)
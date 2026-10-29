from Product import Product
class Inventory:
    def __init__(self):
         self.__inventory_list = []
    
    def product_id_check(self, product_id):
        for product in self.__inventory_list:
            if product.product_id() == product_id: #check if id matches the id in inventory list
                return(True)
        return(False)

    def display_all(self): #option 1
        print("Current Inventory")
        print("-------------------------------------")
        for product in self.__inventory_list: #loop and print
            product.display_information()
        print("-------------------------------------")

    def add_product(self, product): #option 2
        self.__inventory_list.append(product)

    def search_product(self, product_id): #option 4
        print("\nSearch Product")
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
from Product import Product
class Inventory:
    def __init__(self):
         self.__inventory_list = []

    def load_list(self, data): #converts data from json into Product in Inventory
        self.__inventory_list = []
        for product_data in data:
            product = Product(
                product_data["product_id"],
                product_data["name"],
                product_data["price"],
                product_data["stock"]
            )
            self.__inventory_list.append(product)
    
    def product_id_check(self, product_id):
        for product in self.__inventory_list:
            if product.product_id() == product_id: #check if id matches the id in inventory list
                return(product)
        return(None)

    def display_all(self): #option 1
        print("Current Inventory")
        print("-------------------------------------")
        for product in self.__inventory_list: #loop and print
            product.display_information()
        print("-------------------------------------")

    def add_product(self, product): #option 2
        self.__inventory_list.append(product)

    def search_product(self): #option 4
        print("\nSearch Product")
        ProductID= input("Enter Product ID:").capitalize()
        for product in self.__inventory_list:
            if product.product_id() == ProductID: #check if id matches the id in inventory list
                print("\nProduct Found")
                print("-------------------------------------")
                print(f"ID:  {product.product_id()}")
                print(f"Name:  {product.name()}")
                print(f"Price: ${product.price():.2f}")
                print(f"Stock: {product.stock()}")
                print("-------------------------------------")
                return(product) #stops entire function, using break will only exit the if loop
        print("\nProduct not found.")
        return(None) #stops entire function and indicates no results

    def to_list(self): #converts all Product dictionaries to list of dictionaries for json
        return [product.to_dict() for product in self.__inventory_list]
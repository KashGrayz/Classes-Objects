
#Shopping Cart Class

# As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list). 
# As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart. 
# As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)  
# As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart. 
from product import Product

class ShoppingCart:

    def __init__(self, list):
        self.s_cart = Product()

    def total_cart(self):
        self.s_cart = Product() * self.price
        return self.s_cart
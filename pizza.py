"""Provides a Pizza class"""


class Pizza():
    """ Represents Menus and deals for Nature's Pizza

    Attributes:
        menu =  different flavors for pizza
        quantity = number of pizza to order
        size = sizes available for delivery  
        toppings = toppings available for delivery
    """

    def __init__(self, menu, quantity, size, toppings):
        """Initializes a new customer """
        self.menu = menu
        self.quantity = quantity
        self.size = size
        self.toppings = toppings

    def get_menu(self):
        """gets the menu"""
        count = 1
        # print all items in the menu list
        for menu in self.menu:
            print(count,  "- ",  menu)
            count += 1

    def get_size(self):
        """gets the size"""
        count = 1
        # print all items in the size list
        for size, price in self.size.items():
            print(count,  "- ",  size,  " = ",  price)
            count += 1

    def get_toppings(self):
        """gets the size"""
        count = 1
        # print all items in toppings list
        for toppings in self.toppings:
            print(count,  "- ", toppings)
            count += 1

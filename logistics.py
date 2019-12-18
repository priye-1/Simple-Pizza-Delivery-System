# coding=utf-8
"""Provides an account class"""


class Account():
    """ Represents a Customer's account detail for Nature's Pizza

    Attributes:
         account_name = name of the customers account
         account_number = number of the accounnt
         account_password = password for the account

    """

    def __init__(self, cell_number, email, account_name, account_number, account_password):
        """Initializes  new account """
        self.cell_number = cell_number
        self.email = email
        self.account_name = account_name
        self.account_number = account_number
        self.account_password = account_password

    def get_full_describtion(self):
        """print full customers details"""
        print(self.account_name + str(self.account_number) + str(self.account_password))


class Orders():
    """ Represents a Customer's order detail for Nature's Pizza

    Attributes:
         city = city for delivery
         street_no = street number for delivery
         street_name = street name for delivery
    """

    def __init__(self, city, street_no, street_name):
        """Initializes new order for delivery """
        self.city = city
        self.street_no = street_no
        self.street_name = street_name

    def get_delivery(self):
        """prints delivery details"""
        print(self.city + str(self.street_no) + self.street_name)


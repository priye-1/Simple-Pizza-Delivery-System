"""Importing Modules to use predefined functions"""
from logistics import Orders, Account
from pizza import Pizza
import sys

# start program
if True:
    print("**************************************************\n")
    print("*            *Welcome to NATURE's PIZZA*         *\n")
    print("**************************************************")

    # Take Users first choice to proceed into program
    choice1 = str(input("Want to proceed? (y/n): "))

    # Check if user input is not valid
    while (choice1 != "y") and (choice1 != "n"):
        print("\nPlease enter a valid answer")
        choice1 = str(input("\n Want to proceed? (y/n): "))

    # granted permission to proceed with program 
    if (choice1 == "y"):
        
        # display dashboard
        print("\n<<< Dashboard >>>")
        print("1 - To check Menu")
        print("2 - To Check Deals")
        print("3 - To exit Page")

        # receive users second choice from dashboard
        choice2 = int(input(">>> "))

        option = [1, 2, 3]
        options = [1, 2, 3, 4]

        # conditional statements based on user input

        # Check if user input is valid
        while (choice2 not in option):
            print("\nPlease enter a valid option: ")
            choice2 = int(input(">>> "))

        while (choice2 == 2):
            print("\n<<< We have exciting deals just for you! >>>")
            print("----- 30% Off on first orders ")
            print("----- Christmas buy one and get one free")
            print("----- Pepporoni Chicken Combo!")
            choice5 = input("\nWant to make order? (y/n): ")
            if (choice5 == "y"):
                choice2 = 1
            else:
                sys.exit()

        # Creation of lists containing menu and customizations available for Nature's pizza
        # Proceed to view and choose menu   
        if (choice2 == 1):
            menu = ["chicken bali", "pepperoni", "sweet corn", "onion mushroom"]
            quantity = 0
            list_of_size = ["mini", "small", "medium", "large"]
            sizes_and_price = {"mini": 500, "small": 1000, "medium": 3000, "large": 5000}
            toppings = ["cheese", "meat", "sauce", "vegetable"]

            # creates an instance of the Pizza class
            main_menu = Pizza(menu, quantity, sizes_and_price, toppings)
            print("\n<<< Our Menu >>>")

            # call get_menu() function from the Pizza class
            main_menu.get_menu()

            choice3 = str(input("\nProceed to order? (y/n): "))

            # Check if user input is valid
            while (choice3 != "y") and (choice3 != "n"):
                print("\nPlease enter a valid answer")
                choice3 = str(input("\nProceed to order? (y/n): "))

            if choice3 == "y":
                
                # receive customers prefered menu
                prefered_menu = int(
                    input("\nChoose option for prefered menu: "))

                # Check if input is valid 
                while (prefered_menu not in options):
                    print("\nPlease pick options from the menu provided")
                    prefered_menu = int(input(">>> "))

                # access user option from nature's pizza menu using its index
                prefered_menu = menu[prefered_menu - 1]

                # receive number of orders from user
                quantity = int(input("\nHow many orders: "))

                # specifies the maximum amount of orders available at nature's pizza
                while (quantity > 50):
                    print("\nWhy dont we start with orders less than 50?")
                    quantity = int(input(">>> "))

                # Displays available sizes of Pizza
                print("\n<<< Pick Sizes >>>")

                # calls get_size() function from the Pizza Class
                main_menu.get_size()

                # receives user prefered size 
                prefered_size = int(
                    input("\nChoose option for prefered size: "))

                # check if user input is valid
                while (prefered_size not in options):
                    print("\nPlease pick options from the sizes provided")
                    prefered_size = int(input(">>> "))

                # access user prefered size from nature's pizza menu using its index    
                prefered_size = list_of_size[prefered_size - 1]
                price = sizes_and_price[prefered_size]


                # Displays available Toppings for moof Pizza
                print("\n<<< Choose Toppings >>>")

                # calls the get_toppings() method from Pizza Class
                main_menu.get_toppings()
                prefered_toppings = int(input(">>> "))

                # checks if user input is valid
                while (prefered_toppings not in options):
                    print("\nPlease pick options from the toppings provided")
                    prefered_toppings = int(input(">>> "))
                prefered_toppings = toppings[prefered_toppings - 1]

                # storing pizza details in a dictionary
                full_order = {"menu": prefered_menu, "size": prefered_size, "quantity": quantity, "Toppings": prefered_toppings, "price": price}
                print("\n<<< Full Order >>>")
                print(full_order)

                # receive user details for payment procedure and sum total cost
                print("\nProceed TO Payment >>>")
                print("\n>>> Each Delivery costs N500")
                print("\n>>> Total cost: N" + str(price + 500))
                print("\n<<< Kindly fill in the following >>>")
                acct_name = input("Account Name: ")
                acct_number = int(input("Account Number: "))
                password = int(input("Pin: "))
                cell_number = int(input("Cell Number: "))
                email = str(input("Email: "))

                # check if any detail for payment is not filled in
                while (acct_name is None) or (acct_number is None) or (password is None) or (cell_number is None) or (email is None):
                    print("\n<<< You Skipped a field, Please re- fill form >>>")
                    acct_name = input("Account Name: ")
                    acct_number = int(input("\nAccount Number: "))
                    password = int(input("\nPin: "))
                    cell_number = int(input("\nCell Number: "))
                    email = str(input("\nEmail: "))
                    
                # creating an instance of the account class and calling its get_full_describtion() method
                account = Account(
                    cell_number, email, acct_name, acct_number, password)
                account.get_full_describtion()

                # receiving user location for delivery
                print("\n<<< fill in location for delivery >>>")
                list_of_cities = ["abuja", "lagos", "calabar", "delta", "rivers"]
                city = input("\nChoose your city (abuja, lagos, calabar, delta, rivers): ")

                # Check if input is valid
                while (city not in list_of_cities):
                    city = input(
                        "\nSorry We do not deliver to " + city +
                        "\nPlease pick from listed cities(abuja, lagos, calabar, delta, rivers): ")

                street_number = int(input("Street Number: "))
                street_name = str(input("Street Name: "))
                delivery_to = Orders(city, street_number, street_name)

                # file handling 
                if delivery_to:
                    
                    # create new file named NewOrder.txt and write full delivery details to file
                    f = open("NewOrder.txt", "x")
                    f.write("\n***** Order Completed! *****\n\n>>> " + str(
                        quantity) + " " + prefered_size + " sized " + prefered_menu + " pizza (N" + str(price + 500) +
                        ")\n>>> Delivery to " + acct_name + " in " + city + ", street number " + str(
                            street_number) + " in 20 mins or less.\n\n***** Thanks for patronizing! *****")
                    f.close()

                    # open file created and read contents of the text file
                    f = open("NewOrder.txt", "r")
                    print(f.read())
                    sys.exit()
    
            else:
                # End program if users chooses to
                sys.exit()
        else:
            # End program if user chooses to
            sys.exit()

    else:
        sys.exit()



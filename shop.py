# shop.py

import definitions
import utils
from prettytable import PrettyTable
import sys

if __name__ == "__main__":
    print("Welcome to Akshay Stores!\n")
    metadata = utils.login()

    if metadata == 0:
        sys.exit()

    akshay_stores = definitions.Market()
    utils.setup_data_for_testing(akshay_stores)

    if metadata[0] == "SWD":
        check = True
        cart_table = PrettyTable(
            ["Item", "Code", "Quantity", "Original Price", "Price"]
        )
        customer = definitions.Student(metadata[1], metadata[2], metadata[3])
        total = 0
        discount_availed = 0
        while check:
            print("--------------------------------------------")
            print("\n(1) To view the market")
            print("(2) To add an item to your cart")
            print("(3) To remove items from your cart")
            print("(4) To view the items in your cart")
            print("(5) To check out and complete your purchase")
            print("(6) To search for an item in the market\n")
            print("--------------------------------------------")
            option = int(input("Enter your choice: "))

            if option == 1:
                market = akshay_stores.view_market()
                print(market)

            elif option == 2:
                cart_table = PrettyTable(
                    ["Item", "Code", "Quantity", "Original Price", "Price"]
                )
                code = str(input("Enter the item code: ")).upper()
                in_market = akshay_stores.check_item_code(code)
                if type(in_market) == list and in_market[0]:
                    qty = int(input("Enter the quantity: "))
                    customer.add_to_cart(in_market[1], qty)
                    print("Item added succesfully!")
                else:
                    print("Item not found!")
                total, discount_availed = customer.view_cart(cart_table)

            elif option == 3:
                cart_table = PrettyTable(
                    ["Item", "Code", "Quantity", "Original Price", "Price"]
                )
                customer.view_cart(cart_table)
                code = str(input("Enter the item code: ")).upper()
                result, new_total = customer.delete_from_cart(code, total)
                if result is False:
                    print("Item not found!")
                else:
                    print("Item removed!")
                    total = new_total

            elif option == 4:
                cart_table = PrettyTable(
                    ["Item", "Code", "Quantity", "Original Price", "Price"]
                )
                only_view = True
                customer.view_cart(cart_table)
                only_view = False

            elif option == 5:
                cart_table = PrettyTable(
                    ["Item", "Code", "Quantity", "Original Price", "Price"]
                )
                print("----------------------------------------")
                print("AKSHAY SUPERMARKET")
                print(f"Student Name: {metadata[2]}")
                print(f"BITS ID: {metadata[1]}")
                print("Payment method : SWD account")
                only_view = True
                total, discount_availed = customer.view_cart(cart_table)
                print("Total price after CGST (2.7%): ₹", total + 2.7 / 100 * (total))
                print("Total discount availed: ₹", discount_availed)
                print("Thank you for your succesful purchase!\n")
                print("---------------------------------------")
                break

            elif option == 6:
                checker6 = True
                while checker6:
                    print("(1) Search by name")
                    print("(2) Search by code")
                    print("(3) Exit")
                    choice = int(input("Enter yor option: "))
                    if choice == 1:
                        name = str(input("Enter the keyword: "))
                        print(akshay_stores.search_by_name(name))
                    elif choice == 2:
                        code = str(input("Enter the item code: "))
                        print(akshay_stores.search_by_code(code))
                    elif choice == 3:
                        break
                    else:
                        print("Invalid input. Try again \n")

    elif metadata[0] == "no_SWD":
        check = True
        customer = definitions.NonSWDCustomer(
            metadata[1], metadata[2], definitions.isUPI
        )
        cart_table = PrettyTable(
            ["Item", "Code", "Quantity", "Original Price", "Price"]
        )
        total = 0
        discount_availed = 0
        while check:
            print("--------------------------------------------")
            print("\n(1) To view the market")
            print("(2) To add an item to your cart")
            print("(3) To remove items from your cart")
            print("(4) To view the items in your cart")
            print("(5) To check out and complete your purchase")
            print("(6) To search for an item in the market\n")
            print("--------------------------------------------")
            option = int(input("Enter your choice: "))

            if option == 1:
                market = akshay_stores.view_market()
                print(market)

            elif option == 2:
                cart_table = PrettyTable(
                    ["Item", "Code", "Quantity", "Original Price", "Price"]
                )
                code = str(input("Enter the item code: ")).upper()
                in_market = akshay_stores.check_item_code(code)
                if type(in_market) == list and in_market[0]:
                    qty = int(input("Enter the quantity: "))
                    customer.add_to_cart(in_market[1], qty)
                    print("Item added succesfully!")
                else:
                    print("Item not found!")
                total, discount_availed = customer.view_cart(cart_table)

            elif option == 3:
                cart_table = PrettyTable(
                    ["Item", "Code", "Quantity", "Original Price", "Price"]
                )
                customer.view_cart(cart_table)
                code = str(input("Enter the item code: ")).upper()
                result, new_total = customer.delete_from_cart(code, total)
                if result is False:
                    print("Item not found!")
                else:
                    print("Item removed!")
                    total = new_total

            elif option == 4:
                cart_table = PrettyTable(
                    ["Item", "Code", "Quantity", "Original Price", "Price"]
                )
                only_view = True
                customer.view_cart(cart_table)
                only_view = False

            elif option == 5:
                cart_table = PrettyTable(
                    ["Item", "Code", "Quantity", "Original Price", "Price"]
                )
                print("--------------------------------------------")
                print("AKSHAY SUPERMARKET")
                print(f"Student Name: {metadata[2]}")
                print(f"BITS ID: {metadata[1]}")
                print("Payment method : ", end="")
                if definitions.isUPI:
                    print("UPI")
                else:
                    print("CASH")
                only_view = True
                total, discount_availed = customer.view_cart(cart_table)
                print("Total price after CGST (2.7%): ₹", total + 2.7 / 100 * (total))
                print("Total discount availed: ₹", discount_availed)
                print("Thank you for your succesful purchase!\n")
                print("---------------------------------------")
                break

            elif option == 6:
                checker6 = True
                while checker6:
                    print("(1) Search by name")
                    print("(2) Search by code")
                    print("(3) Exit")
                    choice = int(input("Enter yor option: "))
                    if choice == 1:
                        name = str(input("Enter the keyword: "))
                        print(akshay_stores.search_by_name(name))
                    elif choice == 2:
                        code = str(input("Enter the item code: "))
                        print(akshay_stores.search_by_code(code))
                    elif choice == 3:
                        break
                    else:
                        print("Invalid input. Try again \n")
    elif metadata == "admin":
        print("Here is the details of the market along with profits: ")
        print(utils.admin_views(akshay_stores))
    else:
        print("Unexpected error!")

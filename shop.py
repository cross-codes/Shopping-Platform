# shop.py

import definitions
from prettytable import PrettyTable

if __name__ == "__main__":
    print ("Welcome to Akshay Stores!\n")
    metadata = definitions.login()

    if metadata[0] == "SWD":
        check = True
        cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
        customer = definitions.Student(metadata[1], metadata[2], metadata[3])
        total = 0
        discount_availed = 0
        while check:
            print("--------------------------------------------")
            print ("\n(1) To view the market")
            print ("(2) To add an item to your cart")
            print ("(3) To remove items from your cart")
            print ("(4) To view the items in your cart")
            print ("(5) To check out and complete your purchase")
            print ("(6) To search for an item in the market\n")
            print("--------------------------------------------")
            option = int(input("Enter your choice: "))
            market = definitions.view_market(definitions.akshay)

            if option == 1:
                print (market)

            elif option == 2:
                cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
                code = str(input("Enter the item code: ")).upper()
                in_market = definitions.check_item_code(code, definitions.akshay)
                if type(in_market) == list and in_market[0]:
                    qty = int(input("Enter the quantity: "))
                    customer.add_to_cart(in_market[1], qty)
                    print ("Item added succesfully!")
                else:
                    print ("Item not found!")
                total, discount_availed = definitions.view_cart(customer, cart_table)

            elif option == 3:
                cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
                definitions.view_cart(customer, cart_table)
                code = str(input("Enter the item code: ")).upper()
                values = definitions.delete_from_cart(customer, code, total)
                if type(values) == bool:
                    print ("Item not found!")
                else:
                    print ("Item removed!")
                    customer = values[0]
                    total = values[1]

            elif option == 4:
                cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
                only_view = True
                definitions.view_cart(customer, cart_table)
                only_view = False

            elif option == 5:
                cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
                print ("----------------------------------------")
                print ("AKSHAY SUPERMARKET")
                print (f"Student Name: {metadata[2]}")
                print (f"BITS ID: {metadata[1]}")
                print ("Payment method : SWD account")
                only_view = True
                total, discount_availed = definitions.view_cart(customer, cart_table)
                print ("Total price after CGST (2.7%): ", total + 2.7/100*(total))
                print ("Total discount availed: ", discount_availed)
                print ("Thank you for your succesful purchase!\n")
                print ("---------------------------------------")
                break

            elif option == 6:
                pass

    elif metadata[0] == "no_SWD":
        check = True
        customer = definitions.Non_SWD_Customer(metadata[1], metadata[2], definitions.isUPI)
        cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
        total = 0
        discount_availed = 0
        while check:
            print("--------------------------------------------")
            print ("\n(1) To view the market")
            print ("(2) To add an item to your cart")
            print ("(3) To remove items from your cart")
            print ("(4) To view the items in your cart")
            print ("(5) To check out and complete your purchase")
            print ("(6) To search for an item in the market\n")
            print("--------------------------------------------")
            option = int(input("Enter your choice: "))
            market = definitions.view_market(definitions.akshay)

            if option == 1:
                print (market)

            elif option == 2:
                cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
                code = str(input("Enter the item code: ")).upper()
                in_market = definitions.check_item_code(code, definitions.akshay)
                if type(in_market) == list and in_market[0]:
                    qty = int(input("Enter the quantity: "))
                    customer.add_to_cart(in_market[1], qty)
                    print ("Item added succesfully!")
                else:
                    print ("Item not found!")
                total, discount_availed = definitions.view_cart(customer, cart_table)

            elif option == 3:
                cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
                definitions.view_cart(customer, cart_table)
                code = str(input("Enter the item code: ")).upper()
                values = definitions.delete_from_cart(customer, code, total)
                if type(values) == bool:
                    print ("Item not found!")
                else:
                    print ("Item removed!")
                    customer = values[0]
                    total = values[1]

            elif option == 4:
                cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
                only_view = True
                definitions.view_cart(customer, cart_table)
                only_view = False

            elif option == 5:
                cart_table = PrettyTable(["Item", "Code", "Quantity", "Original Price", "Price"])
                print ("--------------------------------------------")
                print ("AKSHAY SUPERMARKET")
                print (f"Student Name: {metadata[2]}")
                print (f"BITS ID: {metadata[1]}")
                print ("Payment method : ", end="")
                if definitions.isUPI:
                    print ("UPI")
                else:
                    print ("CASH")
                only_view = True
                total, discount_availed = definitions.view_cart(customer, cart_table)
                print ("Total price after CGST (2.7%): ", total + 2.7/100*(total))
                print ("Total discount availed: ", discount_availed)
                print ("Thank you for your succesful purchase!\n")
                print ("---------------------------------------")
                break

            elif option == 6:
                pass
    else:
        pass


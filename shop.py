# shop.py

import definitions
from prettytable import PrettyTable

if __name__ == "__main__":
    print ("Welcome to Akshay Stores!\n")
    metadata = definitions.login()

    if metadata[0] == "SWD":
        check = True
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
                customer = definitions.Student(metadata[1], metadata[2], metadata[3])
                code = str(input("Enter the item code: ")).upper()
                in_market = definitions.check_item_code(code, definitions.akshay)
                if type(in_market) == list and in_market[0]:
                    qty = int(input("Enter the quantity: "))
                    customer.add_to_cart(in_market[1], qty)
                    print ("Item added succesfully!")
                else:
                    print ("Item not found!")
                total, discount_availed = definitions.view_cart(customer, cart_table, total, discount_availed)

            elif option == 3:
                customer = definitions.Student(metadata[1], metadata[2], metadata[3])
                definitions.view_cart(customer, cart_table, total)
                code = str(input("Enter the item code: ")).upper()
                definitions.delete_from_cart(customer, code, definitions.akshay)

            elif option == 4:
                only_view = True
                definitions.view_cart(customer, cart_table, total, discount_availed, only_view)
                only_view = False

            elif option == 5:
                print ("----------------------------------------")
                print ("AKSHAY SUPERMARKET")
                print (f"Student Name: {metadata[2]}")
                print (f"BITS ID: {metadata[1]}")
                print ("Payment method : SWD Mess account")
                only_view = True
                total, discount_availed = definitions.view_cart(customer, cart_table, total, discount_availed, only_view)
                print ("Total price after CGST (2.7%): ", total + 2.7/100*(total))
                print ("Total discount availed: ", discount_availed - 2.7/100*(total))
                print ("Thank you for your succesful purchase!\n")
                print ("---------------------------------------")
                break

            elif option == 6:
                pass

    elif metadata[0] == "no_SWD":
        check = True
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
                customer = definitions.Non_SWD_Customer(metadata[1], metadata[2], definitions.isUPI)
                code = str(input("Enter the item code: ")).upper()
                in_market = definitions.check_item_code(code, definitions.akshay)
                if type(in_market) == list and in_market[0]:
                    qty = int(input("Enter the quantity: "))
                    customer.add_to_cart(in_market[1], qty)
                    print ("Item added succesfully!")
                else:
                    print ("Item not found!")
                total, discount_availed = definitions.view_cart(customer, cart_table, total, discount_availed)

            elif option == 3:
                customer = definitions.Non_SWD_Customer(metadata[1], metadata[2], definitions.isUPI)
                definitions.view_cart(customer, cart_table, total)
                code = str(input("Enter the item code: ")).upper()
                definitions.delete_from_cart(customer, code, definitions.akshay)

            elif option == 4:
                only_view = True
                definitions.view_cart(customer, cart_table, total, discount_availed, only_view)
                only_view = False

            elif option == 5:
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
                total, discount_availed = definitions.view_cart(customer, cart_table, total, discount_availed, only_view)
                print ("Total price after CGST (2.7%): ", total + 2.7/100*(total))
                print ("Total discount availed: ", discount_availed - 2.7/100*(total))
                print ("Thank you for your succesful purchase!\n")
                print ("---------------------------------------")
                break

            elif option == 6:
                pass
    else:
        pass


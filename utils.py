# utils

from definitions import Item
from prettytable import PrettyTable
import admin_credentials
import getpass
import random

def login():
    global isUPI
    check_login = True
    while check_login:
        admin_check = int(input(("Would you like to login as a customer (1) or an administrator (2)?: ")))
        if admin_check == 1:
            id = str(input("Enter your BITS ID: "))
            name = str(input("Enter your name: "))
            check_SWD = True
            while check_SWD:
                SWD_check = str(input(f"Hello {name}, would you like to pay with your SWD account? (Y/N): "))
                if SWD_check.upper() == "Y":
                    room_number = str(input("Enter your hostel number: "))
                    return ["SWD", id, name, room_number]
                elif SWD_check.upper() == "N":
                    payment_check = True
                    while payment_check:
                        payment_method = int(input("Would you like to pay using UPI (1) or Cash (2)?: "))
                        if payment_method == 1:
                            isUPI = True
                            return ["no_SWD", id, name]
                        elif payment_method == 2:
                            isUPI = False
                            return ["no_SWD", id, name]
                        else:
                            print ("Invalid input. Try again.\n")
                            payment_check = True
                else:
                    print ("Invalid input. Try again.\n")
                    check_SWD = True
        elif admin_check == 2:
            username = str(input("Enter the administrator username: "))
            pwd = getpass.getpass("Enter the password (hidden for privacy): ")
            if username == admin_credentials.admin_username and pwd == admin_credentials.admin_password:
                return "admin"
            else:
                print ("Incorrect credentials entered")
                return 0
        else:
            print ("Invalid input. Try again.\n")
            admin_check = True

def admin_views(market_obj):
    table = PrettyTable(
        [
            "Name",
            "Category",
            "Cost Price",
            "Original Price",
            "Selling Price",
            "Item Code",
            "Profit per item",
        ]
    )
    for list_item in market_obj.all_items():
        print(list_item)
        for item in list_item:
            print(item)
            table.add_row(Item.return_lst(item))
    return table

def setup_data_for_testing(market_obj):
    discount = 0
    cur_item = None
    i1_f = Item("Lays - Chips", "Food", 15, 20, 20, True, "F1")
    i2_f = Item("Sundrop - Peanut butter", "Food", 150, 175, 175, True, "F2")
    i3_f = Item("Amul - Kool - Coffee flavored milk", "Food", 20, 25, 25, True, "F3")
    i4_f = Item("Lion - Dates", "Food", 130, 132, 132, True, "F4")
    i5_f = Item("Tulsi - Chile Walnuts", "Food", 300, 330, 330, True, "F5")
    food = [i1_f, i2_f, i3_f, i4_f, i5_f]
    for v in range(0, len(food), 1):
        cur_item = food[v]
        discount = random.randrange(0, 10)
        cur_item.set_discount(discount)
        market_obj.add_item(cur_item)

    i1_e = Item(
        "Syska - 50W Miniature light bulb", "Electronics", 80, 100, 100, True, "E1"
    )
    i2_e = Item("Wipro - Table lamp", "Electronics", 150, 200, 200, True, "E2")
    i3_e = Item("Milton - Electric Kettle", "Electronics", 1200, 1500, 1500, True, "E3")
    i4_e = Item(
        "Orient Electric - Electric Heater", "Electronics", 1500, 1600, 1600, True, "E4"
    )
    i5_e = Item(
        "Havells - Electric table fan", "Electronics", 200, 250, 250, True, "E5"
    )
    electronics = [i1_e, i2_e, i3_e, i4_e, i5_e]
    for w in range(0, len(electronics), 1):
        cur_item = electronics[w]
        discount = random.randrange(0, 25)
        cur_item.set_discount(discount)
        market_obj.add_item(cur_item)

    i1_t = Item("Oral B - Toothbrush", "Toiletries", 10, 10, 10, True, "T1")
    i2_t = Item("Lux - Fragrant bar soap", "Toiletries", 35, 37, 37, True, "T2")
    i3_t = Item("Colgate - Toothpaste", "Toiletries", 10, 10, 10, True, "T3")
    i4_t = Item("Ezee - Liquid detergent", "Toiletries", 60, 65, 65, True, "T4")
    i5_t = Item("Vim - Dishwashing liquid", "Toiletries", 55, 55, 55, True, "T5")
    toiletries = [i1_t, i2_t, i3_t, i4_t, i5_t]
    for x in range(0, len(toiletries), 1):
        cur_item = toiletries[x]
        discount = random.randrange(0, 2)
        cur_item.set_discount(discount)
        market_obj.add_item(cur_item)

    i1_s = Item("Ruled 200 pages diary", "Stationery", 250, 270, 270, True, "S1")
    i2_s = Item("ITC - 100 pages ruled notebook", "Stationery", 70, 75, 75, True, "S2")
    i3_s = Item("Reynolds - Ball point pen (pack of 10)","Stationery",100, 100, 100, True, "S3")
    i4_s = Item("DOMS - 15cm scale", "Stationery", 5, 5, 5, True, "S4")
    i5_s = Item("Casio - 991ES Plus Scientific calculator","Stationery",800,900,900,True,"S5",)
    stationery = [i1_s, i2_s, i3_s, i4_s, i5_s]
    for y in range(0, len(stationery), 1):
        cur_item = stationery[y]
        discount = random.randrange(0, 1)
        cur_item.set_discount(discount)
        market_obj.add_item(cur_item)

    i1_c = Item("USPA - Polo T Shirt", "Clothes", 450, 500, 500, True, "C1")
    i2_c = Item("Umbro - Pullover", "Clothes", 1000, 1200, 1200, True, "C2")
    i3_c = Item("Hush Puppies - Sandals", "Clothes", 350, 400, 400, True, "C3")
    i4_c = Item("Jockey - Pack of 5 Men's underwear", "Clothes", 700, 750, 750, True, "C4")
    i5_c = Item("Levis - Cargo pant", "Clothes", 1200, 1300, 1300, True, "C5")
    clothes = [i1_c, i2_c, i3_c, i4_c, i5_c]
    for z in range(0, len(clothes), 1):
        cur_item = clothes[z]
        discount = random.randrange(0, 15)
        cur_item.set_discount(discount)
        market_obj.add_item(cur_item)

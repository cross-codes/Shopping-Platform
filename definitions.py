# definitions.py

from prettytable import PrettyTable

isUPI = False


class Item:
    def __init__(
        self,
        name,
        category,
        _cost_price,
        original_price,
        selling_price,
        is_discounted,
        item_code,
    ):
        self.name = name
        self.category = category
        self.cost_price = _cost_price
        self.original_price = original_price
        self.selling_price = selling_price
        self.is_discounted = is_discounted
        self.item_code = item_code

    def set_discount(self, discount_percentage):
        self.selling_price = self.original_price - self.original_price * (
            discount_percentage / 100
        )

    def money_saved(self):
        if not self.is_discounted:
            return 0
        else:
            return self.original_price - self.selling_price

    def __str__(self):
        return f"{self.name}, {self.category}, {self.cost_price}, {self.original_price}, {self.selling_price}, {self.is_discounted}, {self.item_code}"

    def return_lst_notadmin(self):
        return [
            self.name,
            self.category,
            self.original_price,
            self.selling_price,
            self.item_code,
        ]

    def return_lst(self):
        return [
            self.name,
            self.category,
            self.cost_price,
            self.original_price,
            self.selling_price,
            self.item_code,
            round(self.selling_price - self.cost_price, 2),
        ]


class Market:
    def __init__(self, items={}):
        self.__available_items = items

    def add_item(self, item):
        if item.category in self.__available_items:
            self.__available_items[item.category].append(item)
        else:
            self.__available_items[item.category] = [item]

    def view_market(self):
        table = PrettyTable(
            ["Name", "Category", "Original Price", "Price", "Item Code"]
        )
        for list_item in self.__available_items.values():
            for item in list_item:
                table.add_row(Item.return_lst_notadmin(item))
        return table

    def search_by_name(self, name):
        for list_item in self.__available_items.values():
            for item in list_item:
                if item.name == name:
                    return item
        return None

    def search_by_code(self, code):
        for list_item in self.__available_items.values():
            for item in list_item:
                if item.item_code == code:
                    return item
        return None

    def check_item_code(self, item_code):
        for list_item in self.__available_items.values():
            for item in list_item:
                lst = Item.return_lst_notadmin(item)
                if item_code == lst[4]:
                    return [True, item]
                else:
                    continue
        return False

    def all_items(self):
        return (self.__available_items.values())


class GeneralCustomer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.__cart = {}

    def add_to_cart(self, item, quantity):
        self.__cart[item] = quantity

    def view_cart(self, table, only_view=False):
        total = 0
        discount = 0
        items = list(self.__cart.keys())
        quantities = list(self.__cart.values())
        for x in range(0, len(items), 1):
            if not only_view:
                table.add_row(
                    [
                        items[x].name,
                        items[x].item_code,
                        quantities[x],
                        quantities[x] * items[x].original_price,
                        quantities[x] * items[x].selling_price,
                    ]
                )
                total = total + quantities[x] * items[x].selling_price
                discount = discount + quantities[x] * (items[x].money_saved())
        print(table)
        print("Current total price is: ₹", total)
        return [total, discount]

    def delete_from_cart(self, item_code, cur_total):
        lst = []
        item_lst = []
        for item in self.__cart.keys():
            lst.append(Item.return_lst_notadmin(item))
            item_lst.append(item)
        for z in range(0, len(lst), 1):
            if item_code.upper() == lst[z][4]:
                qty = list(self.__cart.values())[z]
                self.__cart.pop(item_lst[z])
                cur_total = cur_total - lst[z][3] * qty
                return True, cur_total
            else:
                continue
        return False, 0


class Student(GeneralCustomer):
    def __init__(self, id, name, room_number):
        super().__init__(id, name)
        self.room_number = room_number


class NonSWDCustomer(GeneralCustomer):
    def __init__(self, id, name, isUPI):
        super().__init__(id, name)
        self.mode_of_payment = "UPI" if isUPI else "CASH"


from enum import Enum
from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import datetime


class StateOfOrder(Enum):
    PROCESSING, DELIVERED = 1, 2, 3

class ProductCategory(Enum):
    CLOTHING, SHOES, ELECTRONICS = 1, 2, 3

class CreditCard:
    def __init__(self, owner, id, budget):
        self.__owner = owner
        self.__id = id
        self.__budget = budget


    def pay(self, amount):
        self.__budget -= amount


class Etransfer:
    def __init__(self, owner, id, budget):
        self.__owner = owner
        self.__id = id
        self.__budget = budget

    def pay(self, amount):
        self.__budget -= amount


class Transaction:
    def __init__(self, wallet, amount):
        self.__transaction_type = wallet
        self.__amount = amount

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount


class Payment:
    def __init__(self, transaction):
        self.__transaction = transaction

    def make_payment(self):
        self.transaction.get_transaction_type().pay(self.transaction.get_amount())




class Review:
    def __init__(self, text = None, rate = None):
        self.__text = text
        self.__rate = rate



class Product:
    def __init__(self, name, product_category, price, delivery_time):
        self.__name = name
        self.__product_category = product_category
        self.__price = price
        self.__delivery_time = delivery_time
        self.__reviews = []


    def get_name(self):
        return self.__name

    def get_product_category(self):
        return self.__product_category

    def get_price(self):
        return self.__price

    def get_delivery_time(self):
        return self.__delivery_time

    def get_reviews(self):
        return self.__reviews

    def add_review(self, review):
        self.__reviews.append(review)


class Catalog:
    def __init__(self):
        self.__products = set()
        self.__product_titles = defaultdict(Product)
        self.__product_categories = defaultdict(Product)

    def get_products(self):
        return self.__products

    def get_product_by_title(self, title):
        return self.__product_titles[title]

    def get_product_by_category(self, category):
        return self.__product_categories[category]

    def add_product(self, product):
        self.__products.add(product)
        self.__product_titles[product.get_name()] = product
        self.__product_categories[product.get_product_category()] = product

    def remove_product(self, product):
        self.__products.remove(product)
        del self.__product_titles[product.get_name()]
        del self.__product_categories[product.get_product_category()]



class ShoppingCart:
    def __init__(self):
        self.__products = set()


    def get_products(self):
        return self.__products

    def add_product(self, product):
        self.__products.add(product)

    def remove_product(self, product):
        self.__products.remove(product)


class Order:
    def __init__(self, customer, product, delivery_time):
        self.__customer = customer
        self.__product = product
        self.__order_time = datetime.now()
        self.__delivery_time = self.__order_time + delivery_time
        self.__order_status = StateOfOrder.PROCESSING


    def get_status(self):
        return self.__order_status

    def change_status(self):
        self.__order_status = StateOfOrder.DELIVERED

    def remove_product_from_catalog(self, catalog):
        catalog.remove_product(self.__product)


class Account(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def search_product_by_title(self, title, catalog):
        return catalog.get_product_by_title(title)

    def search_product_by_category(self, category):
        return catalog.get_product_by_category

    def view_products(self, catalog):
        return catalog.get_products()


class Guest:
    def __init__(self):
        super().__init__()
    

    def register(self):
        pass


class Customer:
    def __init__(self, username, password, credit_budget, e_transfer_budget):
        super().__init__()
        self.__username = username
        self.__password = password
        self.__shopping_cart = ShoppingCart()   # get shoppingcart methodu mu olmaliu
        self.__credit_card = CreditCard(self.__username, credit_budget)
        self.__e_transfer = Etransfer(self.__username, e_transfer_budget)
        self.__orders = defaultdict(Order)

    def add_product_to_shopping_cart(self, product):
        self.__shopping_cart.add_product(product)

    def remove_product_from_shopping_cart(self, product):
        self.__shopping_cart.remove_product(product)

    def pay_with_card(self, amount):
        transaction = Transaction(self.__credit_card, amount)
        payment = Payment(transaction)
        payment.make_payment()


    #catalog burada parametre olarak mi gelmeli, yoksa customer catalog.get() filan mi yapmali yada initialize ederken im olmali
    #2 orders dictionary product key oldu ama o producti nasil elde edecegiz id vs mi olmali
    def buy_product(self, product, catalog):
        order = Order(self, product, product.get_delivery_time())
        self.__orders[product] = order
        order.remove_product_from_catalog(catalog)


    def make_review(self, product, review):
        product.add_review(review)

    
    def cancel_order(self):
        pass

    #mesela burada producti nasil elde edecek
    def see_order_status(self, product):
        return self.__orders[product].get_status()






    












    

    
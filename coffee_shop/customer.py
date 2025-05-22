
from coffee_shop.coffee import Coffee
class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 1 <= len(value) <= 15:
            raise ValueError("Name must be a string (1-15 characters).")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        customers_spending = {}
        for order in coffee.orders():
            customers_spending[order.customer] = customers_spending.get(order.customer, 0) + order.price
        return max(customers_spending, key=customers_spending.get) if customers_spending else None
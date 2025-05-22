from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer
from coffee_shop.order import Order

def test_coffee_creation():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"

def test_num_orders():
    coffee = Coffee("Americano")
    customer = Customer("Charlie")
    Order(customer, coffee, 3.5)
    assert coffee.num_orders() == 1

def test_average_price():
    coffee = Coffee("Cappuccino")
    customer = Customer("Dana")
    Order(customer, coffee, 4.0)
    Order(customer, coffee, 6.0)
    assert coffee.average_price() == 5.0
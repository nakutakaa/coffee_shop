from coffee_shop.order import Order
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_order_creation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.price == 5.0

def test_invalid_price():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    try:
        Order(customer, coffee, 15.0)  # Invalid price
        assert False
    except ValueError:
        assert True
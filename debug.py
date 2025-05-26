from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

# Sample Usage
customer = Customer("Alice")
coffee = Coffee("Latte")
order = Order(customer, coffee, 5.0)

print(f"{customer.name} ordered {coffee.name} for ${order.price}")
from customer import Customer
from coffee import Coffee
from order import Order

# Sample Usage
customer = Customer("Alice")
coffee = Coffee("Latte")
order = Order(customer, coffee, 5.0)

print(f"{customer.name} ordered {coffee.name} for ${order.price}")
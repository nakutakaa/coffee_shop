from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee  
from coffee_shop.order import Order    

def test_customer_creation():
    """Test that a customer can be created with a valid name."""
    customer = Customer("Alice")
    assert customer.name == "Alice"
def test_relationship_methods():
    customer = Customer("Eve")
    coffee = Coffee("Flat White")
    order = Order(customer, coffee, 4.5)
    
    assert order in customer.orders()
    assert coffee in customer.coffees()

def test_most_aficionado():
    coffee = Coffee("Latte")
    fan = Customer("Super Fan")
    casual = Customer("Casual Drinker")
    
    Order(fan, coffee, 8.0)
    Order(fan, coffee, 7.0)
    Order(casual, coffee, 5.0)
    
    assert Customer.most_aficionado(coffee) == fan    
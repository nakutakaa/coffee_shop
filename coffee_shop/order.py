class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        customer.orders().append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float) or not 1.0 <= value <= 10.0:
            raise ValueError("Price must be a float (1.0-10.0).")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from coffee_shop.customer import Customer  # Moved import here
        if not isinstance(value, Customer):
            raise ValueError("Must be a Customer instance.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee_shop.coffee import Coffee  # Moved import here
        if not isinstance(value, Coffee):
            raise ValueError("Must be a Coffee instance.")
        self._coffee = value
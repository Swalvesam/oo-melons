"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, shipped, order_type, tax, country_code):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code
            
    def get_total(self):
        base_price = 5
        
        if self.species == "christmas melons":
            base_price = base_price * 1.5
        
        total = ((1 + self.tax) * self.qty * base_price)
        return total

    def mark_shipped(self):
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        # self.tax = 0.08

        super().__init__(species, qty, False, "domestic", 0.08, USA)

    def get_total(self):
        """Calculate price, including tax."""
        
        # base_price = 5
        # total = (1 + self.tax) * self.qty * base_price

        print(super().get_total())

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        # self.shipped = True

        return super().mark_shipped()


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.country_code = country_code
        #self.shipped = False
        #self.order_type = "international"
        #self.tax = 0.17
        super().__init__(species, qty, False, "international", 0.17, country_code)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        flat_fee = 3
        if self.qty <= 10:
            total = ((1 + self.tax) * self.qty * base_price) + flat_fee
        else:
            total = (1 + self.tax) * self.qty * base_price 

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        # self.shipped = True
        return super().mark_shipped()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super().__init__(species, qty, False, "government", 0.0, 1)  
        self.passed_inspection = self.mark_inspection     

    def mark_inspection(self, passed):
        self.passed_inspection = "passed" 


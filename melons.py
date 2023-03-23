"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code = None):
        """Initialize melon order attributes."""
       
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # tax = 0
 
class DomesticMelonOrder:
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08

class InternationalMelonOrder:
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
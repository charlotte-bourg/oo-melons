"""Classes for melon orders."""
import random
import datetime

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code = None):
        """Initialize melon order attributes."""
       
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        
    def get_base_price(self):
        datetime.weekday() #integer representing day of week; monday = 0 
        datetime.time.hour() #hour of day
        #if datetime.weekday() in range(0,5) and datetime.time.time in range(8,11)
        return random.randint(5,9)
    
    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
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
 
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def get_total(self):
        base_total = super().get_total()
        if self.qty < 10:
            return base_total + 3
        else:
            return base_total

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""
    order_type = "government"
    tax = 0
    #passed_inspection = False

    def __init__(self, passed):
        super().__init__()
        self.passed_inspection = passed
        
    def mark_inspection(self, passed):
        self.passed_inspection = passed
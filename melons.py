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
        if self.qty > 100:
            raise TooManyMelonsError

    @staticmethod  
    def get_base_price():
        
        current_datetime = datetime.datetime.now()
        day_of_week = current_datetime.weekday() # integer representing day of week; monday = 0 
        hour = current_datetime.hour

        base_price = random.randint(5,9)

        if day_of_week in range(0,5) and hour in range(8,11): 
            base_price += 4
        return base_price
    
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

class TooManyMelonsError(ValueError):
    "Raised when order quantity is > 100"
    def __init__(self, message = "No more than 100 melons!"):
        self.message = message
        super().__init__(self.message)
 
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
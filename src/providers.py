from faker import Faker
from faker.providers import BaseProvider
from datetime import datetime
import uuid
# -----------------------------------------------------
# Customer Providers
# ----------------------------------------------------
def generate_short_id(prefix="CUST"):
    short_unique = uuid.uuid4().hex[:8]
    return f"{prefix}-{short_unique}".upper()
class CustomerProvider(BaseProvider):
    """Custom Provider to generate specific fields for Customer Data"""
    def customer_id(self):
        return generate_short_id()
    
    def gender(self):
        return self.random_element(["M", "F", "U"])

    def signup_channel(self):
        channels = ["Web", "Mobile_App", "Retail_Partner", "Affiliate"]
        return self.random_element(channels)
    
    def signup_promocode(self):
        promocodes = ["SUMMER50", "FREE_SIM_BUNDLE", "FREE_DATA_BUNDLE", "FREE_VOICE_BUNDLE", None]
        return self.random_element(promocodes)
    
    def previous_carier(self):
        carriers = [f"Carrier_{x}" for x in ["A", "B", "C", "D", "E", "F"]]
        carriers.append(None)
        return self.random_element(carriers)
    
    def reg_device_tac(self):
        return str(uuid.uuid4())

    def payment_method(self):
        payment_methods = ["Credit_Card", "Apple_Pay", "Google_Pay", "Debit_Card"]
        return self.random_element(payment_methods)
    

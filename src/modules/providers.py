import random
from datetime import datetime
import uuid

from faker import Faker
from faker.providers import BaseProvider
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
    
    def termination_date(self):
        start_date = datetime(2020,1,1)
        end_date = datetime.now()
        random_date = Faker().date_between(start_date=start_date, end_date=end_date).isoformat()
        choices = [random_date, None]
        return random.choices(choices, weights=[0.25,0.75], k=1)[0]
    def gender(self):
        return self.random_element(["M", "F", "U"])

    def signup_channel(self):
        channels = ["Web", "Mobile_App", "Retail_Partner", "Affiliate"]
        return self.random_element(channels)
    
    def signup_promocode(self):
        promocodes = ["SUMMER50", "FREE_SIM_BUNDLE", "FREE_DATA_BUNDLE", "FREE_VOICE_BUNDLE", None]
        return self.random_element(promocodes)
    
    def previous_carrier(self):
        carriers = [f"Carrier_{x}" for x in ["A", "B", "C", "D", "E", "F"]]
        carriers.append(None)
        return self.random_element(carriers)
    
    def plan_id(self):
        plan_ids = list(range(1, 6, 1))
        return self.random_element(plan_ids)
    
    def reg_device_tac(self):
        return str(uuid.uuid4())

    def payment_method(self):
        payment_methods = ["Credit_Card", "Apple_Pay", "Google_Pay", "Debit_Card"]
        return self.random_element(payment_methods)


class DeviceProvider(BaseProvider):
    
    def fake_msisdn(self):
        def generate_za_msisdn():
            prefixes = [
                "60", "61", "62", "63","64" ,"65",
                "71", "72", "73", "74", "75", "76",
                "81", "82", "83", "84", "85"
            ]
            prefix = random.choice(prefixes)
            subscriber_number = "".join(str(random.randint(0,0)) for _ in range(7))
            return f"27{prefix}{subscriber_number}"
        fake_msisdn = generate_za_msisdn()
        return fake_msisdn
    
    def imsi(self):
        def generate_sa_imsi():
            mcc = "655"
            mnc_options= [
                "01", "10", "07", "02"
            ]
            mnc_weights = [0.25,0.25,0.25,0.25]
            mnc = random.choices(population=mnc_options, weights=mnc_weights, k=1)[0]
            msin = "".join(str(random.randint(0,9)) for _ in range(10))
            return f"{mcc}{mnc}{msin}"
        fake_imsi = generate_sa_imsi()
        return fake_imsi
    
    def imei(self):
        return f"35875111{random.randint(1000000, 9999999)}"
    
    def device_status(self):
        statuses = ["Active", "Suspended", "Replaced"]
        return self.random_element(statuses)
    

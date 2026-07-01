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
    

class ProductProvider(BaseProvider):
    def __init__(self, generator):
        super().__init__(generator)
        self.product_names = [
            "TikTok & Chill Starter", "Social Storm Unlimited",
            "The Infinite Scroll", "Ping Master Elite",
            "Light & Easy Monthly",
        ]
        self.plan_ids = list(range(1,6,1))
        self.generator.random.shuffle(self.product_names)
        self.generator.random.shuffle(self.plan_ids)

    def product_id(self):
        return generate_short_id(prefix="PROD")
    
    def plan_id(self):
        if not self.plan_ids:
            raise ValueError("Exhausted all unique plan ids in the pool!")
        return self.plan_ids.pop()
    
    
    def product_name(self):
        if not self.product_names:
            raise ValueError("Exhausted all unique product names in the pool!")
        return self.product_names.pop()
        
    def product_type(self):
        product_types = [
            "BASE_PLAN", "DATA_ADDON", "ROAMING_PASS", "VOICE_ADDON", "SMS_ADDON"
        ]
        return self.random_element(product_types)
    def billing_type(self):
        billing_types = [
            "Postpaid", "Prepaid"
        ]
        return self.random_element(billing_types)
    def product_price(self):
        random_prices = [
            -1, 30, 45, 99, 50, 99, 149
        ]
        return self.random_element(random_prices)
    
    def data_gb_allowance(self):
        gb_allowance_spread = [
            -1, 0, 1, 2, 3, 5, 8, 13, 21
        ]
        return self.random_element(gb_allowance_spread)
    def voice_minutes_allowance(self):
        voice_minutes_spread = [
            -1, 0, 5, 10, 15, 25, 40, 65, 105, 170
        ]
        return self.random_element(voice_minutes_spread)
    def sms_count_allowance(self):
        sms_count_spread = [
            -1, 0, 10, 30, 40, 70, 110
        ]
        return self.random_element(sms_count_spread)
    


class CallDetailRecordProvider(BaseProvider):
    def generate_za_msisdn(self):
        prefixes = [
            "60", "61", "62", "63","64" ,"65",
            "71", "72", "73", "74", "75", "76",
            "81", "82", "83", "84", "85"
        ]
        prefix = random.choice(prefixes)
        subscriber_number = "".join(str(random.randint(0,0)) for _ in range(7))
        return f"27{prefix}{subscriber_number}"
    
    def determine_bytes_used(self, channel:str):

        if channel == "Retail_Partner" or channel == "Affiliate":
            return random.randint(a=512, b=2*1024*1024)
        else:
            return random.randint(a=1*1024*1024, b=75*1024*1024)
    
    def record_detail(self):
        return str(uuid.uuid4())
    def originating_point(self):
        return self.generate_za_msisdn()
    def cdr_type(self):
        cdr_types = ["voice", "data", "sms"]
        cdr_weights = [0.75, 0.15, 0.1]
        return random.choices(population=cdr_types, weights=cdr_weights, k=1)[0]
        
    def cdr_direction(self, cdr_type:str):
        direction_choices = ["originating", "terminating"]

        if cdr_type == "voice":
            direction_weights = [0.75, 0.25]
        elif cdr_type == "data":
            direction_weights = [0.95, 0.05]
        else:
            direction_weights = [0.55, 0.45]
        
        return random.choices(population=direction_choices, weights=direction_weights, k=1)[0]
    
    def create_datetime_start(self, customer_registration_datetime:str):
        start_datetime = datetime.fromisoformat(customer_registration_datetime)
        end_datetime = datetime(2026,6,1)
        random_datetime = Faker().date_time_between(start_date=start_datetime, end_date=end_datetime).isoformat()
        return random_datetime
    

    def create_session_duration(self, cdr_type:str):
        # duration of session in seconds for voice and data
        # number of messages for sms
        # 0 for unsuccessful sessions
        if cdr_type == "voice" or cdr_type == "data":
            duration_spread = random.randint(0, 3600)
        else:
            duration_spread = random.randint(0, 10)
        return duration_spread
    
    def create_session_size(self, cdr_type:str, signup_channel:str):
        if cdr_type == "data":
            size = self.determine_bytes_used(channel=signup_channel)
        else:
            size = 0
        return size
    
        
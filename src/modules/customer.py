from datetime import datetime
from modules.data_generator import BaseDataGenerator
from modules.providers import CustomerProvider


# ----------------------------------------------------
# Customer
# ---------------------------------------------------
class Customer:
    def __init__(
            self, 
            customer_id:str, registration_date:str,
            termination_date, date_of_birth:str,
            gender:str, signup_channel:str,
            signup_promo_code:str, ported_in_status:bool,
            previous_carrier:str, plan_id:int,
            boyd:str, registration_device_tac:str,
            payment_method:str) -> None:
        
        self.customer_id = customer_id
        self.registration_date = registration_date
        self.termination_date = termination_date
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.signup_channel = signup_channel
        self.signup_promo_code = signup_promo_code
        self.ported_in_status = ported_in_status
        self.previous_carrier = previous_carrier
        self.plan_id = plan_id
        self.boyd = boyd
        self.registration_device_tac = registration_device_tac
        self.payment_method = payment_method
    
    def __repr__(self) -> str:
        return f"Customer(customer_id='{self.customer_id}')"
    
    def to_dict(self):
        return self.__dict__

class CustomerDevice:
    def __init__(
            self, 
            customer_id:str, registration_date:str,
            termination_date, date_of_birth:str,
            gender:str, signup_channel:str,
            signup_promo_code:str, ported_in_status:bool,
            previous_carrier:str, plan_id:int,
            boyd:str, registration_device_tac:str,
            payment_method:str,
            msisdn:str, imsi:str, imei:str, status:str, activated_at:str
            ) -> None:
        
        self.customer_id = customer_id
        self.registration_date = registration_date
        self.termination_date = termination_date
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.signup_channel = signup_channel
        self.signup_promo_code = signup_promo_code
        self.ported_in_status = ported_in_status
        self.previous_carrier = previous_carrier
        self.plan_id = plan_id
        self.boyd = boyd
        self.registration_device_tac = registration_device_tac
        self.payment_method = payment_method,
        self.msisdn = msisdn
        self.imsi = imsi
        self.imei = imei
        self.status = status
        self.activated_at = activated_at
# --------------------------------------------------
# CustomerFactory
# ---------------------------------------------------
class CustomerFactory(BaseDataGenerator):
    def __init__(self, seed=None) -> None:
        if seed is not None:
            super().__init__(seed=seed)
        else:
            super().__init__()
        
        # add providers
        self.fake.add_provider(CustomerProvider)
    
    def generate_customer(self) -> Customer:
        start = datetime(2020,1,1)
        end = datetime.now().date()

        customer = {
           "customer_id": self.fake.customer_id(),
           "registration_date":self.fake.date_time_between(start_date=start, end_date=end).isoformat(), # registration date
           "termination_date": self.fake.termination_date(),
           "date_of_birth":self.fake.date_between(start_date=datetime(1920,1,1), end_date=datetime(2008,1,1)), # dob
           "gender": self.fake.gender(),
           "signup_channel": self.fake.signup_channel(),
           "signup_promo_code": self.fake.signup_promocode(),
           "ported_in_status": self.fake.boolean(),
           "previous_carrier": self.fake.previous_carrier(),
           "plan_id": self.fake.plan_id(), # foreign key to product?
           "boyd": self.fake.boolean(),
           "registration_device_tac": self.fake.reg_device_tac(),
           "payment_method": self.fake.payment_method(),
        }

        return Customer(**customer)
from datetime import datetime
from data_generator import BaseDataGenerator
from providers import CustomerProvider

# --------------------------------------------------
# CustomerFactory
# ---------------------------------------------------
class CustomerFactory(BaseDataGenerator):
    def __init__(self, seed) -> None:
        super().__init__(seed=seed)
        # add providers
        self.fake.add_provider(CustomerProvider)
    
    def generate_customer(self):
        start = datetime(2020,1,1)
        end = datetime.now().date()

        return {
           "customer_id": self.fake.customer_id(),
           "registration_date":self.fake.date_time_between(start_date=start, end_date=end).isoformat(), # registration date
           "termination_date": None,
           "date_of_birth":self.fake.date_between(start_date=datetime(1920,1,1), end_date=datetime(2008,1,1)), # dob
           "gender": self.fake.gender(),
           "signup_channel": self.fake.signup_channel(),
           "signup_promo_code": self.fake.signup_promocode(),
           "ported_in_status": self.fake.boolean(),
           "previous_carrier": self.fake.previous_carrier(),
           "plan_id": self.fake.plan_id(), # foreign key to product?
           "boyd": self.fake.boolean(),
           "registration_device_tac": self.fake.reg_device_tac(),
           "payment_method": self.payment_method(),
        
        }
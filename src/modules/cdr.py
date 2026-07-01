from datetime import datetime
from pathlib import Path
import random
from typing import Dict, Hashable, Union

import pandas as pd 
from modules.data_generator import BaseDataGenerator
from modules.providers import CallDetailRecordProvider

# -----------------------------------------------------
# CDR Class
# --------------------------------------------------

# -----------------------------------------------------------------
# CDR Factory
# ----------------------------------------------------------------

class CallDetailRecordFactory(BaseDataGenerator):
    def __init__(self, seed=None) -> None:
        if seed is not None:
            super().__init__(seed=seed)
        else:
            super().__init__()
        
        # add providers
        self.fake.add_provider(CallDetailRecordProvider)

        self.mvno_products = self.get_mvno_products()
    
    def get_mvno_products(self):
        SCRIPT_DIR = Path(__file__).resolve().parent
        TARGET_DIR = SCRIPT_DIR.parent.parent / "data" / "products"
        file_path  = TARGET_DIR / "products.csv"
        df = pd.read_csv(file_path)
        return df
    
    def get_call_record_product(self, plan_id:str)-> Dict[Hashable|str, Union[int, str]]:
        df = self.mvno_products
        product = df.loc[df["plan_id"] == plan_id].iloc[0].to_dict()
        return product
    def get_call_record_date(self, date_string:str):
        return datetime.fromisoformat(date_string).date()
    
    def get_call_record_month(self, date_string:str):
        return datetime.fromisoformat(date_string)
    def generate_random_number_of_sessions(self):
        return random.randint(a=0, b=50)
    
    def calculate_allowance_balance(self, current_balance:int, amount_used:int):
        if current_balance == -1:
            return -1
        new_balance = current_balance - amount_used
        return new_balance

        
    def generate_call_detail_record(self, customer):
        # start year - get when customer started
        call_detail_start_date = self.get_call_record_date(date_string=customer.registration_date)
        print(customer.termination_date, type(customer.termination_date))
        call_detail_end_date = self.get_call_record_date(date_string=customer.termination_date) if customer.termination_date is not None else datetime.now().date()
        customer_cdrs = []
        while call_detail_start_date <= call_detail_end_date:
            # randomly assign a product to customer
            customer_plan_id = customer.plan_id
            customer_product = self.get_call_record_product(plan_id=customer_plan_id)
            monthly_data_allowance = customer_product.get("data_gb_allowance") * 1024 * 1024 # type: ignore
            monthly_voice_allowance = customer_product.get("voice_minutes_allowance") * 60 # type: ignore
            monthly_sms_allowance = customer_product.get("sms_count_allowance")

            number_of_cdr_sessions = self.generate_random_number_of_sessions()
            for session in range(number_of_cdr_sessions):
                # generate record detail
                record_detail = self.fake.record_detail()
                # set owner of cdr
                subscriber_cli = customer.msisdn
                # set cdr type
                cdr_type = self.fake.cdr_type()
                # set cdr direction
                cdr_direction = self.fake.cdr_direction(cdr_type=cdr_type)
                
                originating_point = subscriber_cli if cdr_direction == "originating" else self.fake.generate_za_msisdn()
                destination_point = subscriber_cli if cdr_direction == "terminating" else self.fake.generate_za_msisdn()
                # set datetime start
                print(call_detail_start_date)
                datetime_start = self.fake.date_time_between(start_date=call_detail_start_date, end_date=call_detail_start_date)#create_datetime_start(customer_registration_datetime=customer.registration_date)
                # set datetime end 
                datetime_end = None
                # set session duration - voice, sms, data
                session_duration = self.fake.create_session_duration(cdr_type=cdr_type)
                # set session size
                session_size = self.fake.create_session_size(cdr_type=cdr_type, signup_channel=customer.signup_channel)
                price=0
                if cdr_direction == "originating":
                    if cdr_type == "voice":
                        if monthly_voice_allowance != 0:
                            price = 0
                            monthly_voice_allowance = self.calculate_allowance_balance(current_balance=monthly_voice_allowance, amount_used=session_duration) # type: ignore
                        else:
                            price = 0.2
                    elif cdr_type == "data":
                        if monthly_data_allowance != 0:
                            price = 0
                            monthly_data_allowance = self.calculate_allowance_balance(current_balance=monthly_data_allowance, amount_used=session_size) # type: ignore
                        else:
                            price = 0.05
                    else:
                        if monthly_sms_allowance != 0:
                            price = 0
                            monthly_sms_allowance = self.calculate_allowance_balance(current_balance=monthly_sms_allowance, amount_used=session_duration) # type: ignore
                        else:
                            price = 0.1
                            
                data_balance = monthly_data_allowance
                voice_balance = monthly_voice_allowance
                sms_balance = monthly_sms_allowance

                cdr_record = {
                    "record_detail": record_detail,
                    "subscriber_cli": subscriber_cli,
                    "originating_point": originating_point,
                    "destination_point": destination_point,
                    "cdr_type": cdr_type,
                    "cdr_direction": cdr_direction,
                    "datetime_start": datetime_start,
                    "datetime_end": datetime_end,
                    "session_duration": session_duration,
                    "session_size": session_size,
                    "data_balance": data_balance,
                    "voice_balance": voice_balance,
                    "sms_balance": sms_balance,
                    "price": price
                }

                customer_cdrs.append(cdr_record)
            next_month = call_detail_start_date.month + random.randint(1, 3)
            next_year = call_detail_start_date.year
            if next_month > 12:
                next_month = 1
                next_year += 1
            call_detail_start_date = datetime(next_year, next_month, 1).date()





        
        # end year - if not terminated set to now() else year terminated
        # for each month between these years
        # randomly assign a product to customer
        # generate a random integer between 0 and 50 as cdr sessions
        # generate a session that consumes from product allowance
        # if cdr sessions finish product allowance before cdr sessions complete
        # set to oob price  

        



        return customer_cdrs
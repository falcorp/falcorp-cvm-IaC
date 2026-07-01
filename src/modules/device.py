from datetime import datetime
from typing import Dict
from modules.data_generator import BaseDataGenerator
from modules.customer import Customer, CustomerFactory
from modules.providers import DeviceProvider

# ------------------------------------------------------------------
# Device
# -------------------------------------------------------
class Device:
    def __init__(self, customer:Customer,
                 msisdn:str, imsi:str, imei:str, status:str):
         self.customer = customer
         self.msisdn = msisdn
         self.imsi = imsi
         self.imei = imei
         self.status = status
         self.activated_at = customer.registration_date

    def to_dict(self):
        return {
            **self.customer.to_dict(),
            "msisdn": self.msisdn,
            "imsi": self.imsi,
            "imei": self.imei,
            "status": self.status,
            "activated_at": self.activated_at
        }
# ------------------------------------------------------------
# Device Factory
# -----------------------------------------------------------

class DeviceFactory(BaseDataGenerator):
    def __init__(self, seed=None):
        if seed is not None:
            super().__init__(seed=seed)
        else:
            super().__init__()
        self.fake.add_provider(DeviceProvider)

    def generate_device_information(self, customer:Customer):
        device_data =  {
            "msisdn": self.fake.fake_msisdn(),
            "imsi": self.fake.imsi(),
            "imei": self.fake.imei(),
            "status": self.fake.device_status(),
        }

        return Device(customer=customer, **device_data)
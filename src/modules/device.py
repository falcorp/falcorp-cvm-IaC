from datetime import datetime
from typing import Dict
from modules.data_generator import BaseDataGenerator
from modules.customer import CustomerFactory
from modules.providers import DeviceProvider

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

    def generate_device_information(self, customer:Dict[str,str]):
        device_data =  {
            "msisdn": self.fake.fake_msisdn(),
            "imsi": self.fake.imsi(),
            "imei": self.fake.imei(),
            "status": self.fake.device_status(),
            "activated_at": customer.get("registration_date")
        }

        return {**customer, **device_data}
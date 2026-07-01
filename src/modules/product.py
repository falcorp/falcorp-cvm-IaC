from datetime import datetime
from modules.data_generator import BaseDataGenerator
from modules.providers import ProductProvider

# -----------------------------------------------------------
# ProductFactory
# -----------------------------------------------------------
class ProductFactory(BaseDataGenerator):
    def __init__(self, seed=None) -> None:
        if seed is not None:
            super().__init__(seed=seed)
        else:
            super().__init__()
        # add providers
        self.fake.add_provider(ProductProvider)
    def generate_product(self):
        return {
            "product_id":self.fake.product_id(),
            "plan_id": self.fake.plan_id(),
            "product_name": self.fake.product_name(),
            "product_type": self.fake.product_type(),
            "billing_type": self.fake.billing_type(),
            "product_price": self.fake.product_price(),
            "data_gb_allowance": self.fake.data_gb_allowance(),
            "voice_minutes_allowance": self.fake.voice_minutes_allowance(),
            "sms_count_allowance": self.fake.sms_count_allowance()

        }
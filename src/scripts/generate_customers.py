import random

import pandas as pd
from pathlib import Path
import os
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules.customer import CustomerFactory
from modules.device import DeviceFactory

def stream_devices(customers):
    possible_devices = list(range(1,6))
    device_factory = DeviceFactory(seed=SEED)
    for customer in customers:
        # determine number of devices to be generated for customer
        no_devices = random.choices(population=possible_devices, weights=[0.5, 0.2, 0.15, 0.1, 0.05], k=1)[0]
        for _ in range(no_devices):
            yield device_factory.generate_device_information(customer=customer)


if __name__ == "__main__":
    # check for args - number of customers to be generated
    SCRIPT_DIR = Path(__file__).resolve().parent
    TARGET_DIR = SCRIPT_DIR.parent.parent / "data" / "customers"
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    SEED = 42
    number_of_customers = 25000
    customer_factory = CustomerFactory(seed=SEED)
    
    customer_generator = (customer_factory.generate_customer().to_dict() for _ in range(number_of_customers))
        
    device_generator = stream_devices(customer_generator)

    df = pd.DataFrame(customer_generator)
    file_path = TARGET_DIR / "customers.csv"

    df.to_csv(file_path, index=False)
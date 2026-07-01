import random

import pandas as pd
from pathlib import Path
import os
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules.customer import Customer, CustomerFactory
from modules.device import DeviceFactory


if __name__ == "__main__":
    # check for args - number of customers to be generated
    SCRIPT_DIR = Path(__file__).resolve().parent
    TARGET_DIR = SCRIPT_DIR.parent.parent / "data" / "devices"
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    SEED = 42

    device_factory = DeviceFactory(seed=SEED)
    # get customer directory
    customer_file_path = SCRIPT_DIR.parent.parent / "data" / "customers" / "customers.csv"
    df = pd.read_csv(customer_file_path)
    # get unique customer ids
    customer_ids = df["customer_id"].unique().tolist()
    def stream_devices(customer_ids):
        for customer_id in customer_ids:
            customer = Customer(**df.loc[df["customer_id"] == customer_id].iloc[0].to_dict())
            number_devices = random.randint(1,2)
            for _ in range(number_devices):
                # create a device
                yield device_factory.generate_device_information(customer=customer).to_dict()
    device_generator = stream_devices(customer_ids)
    
    df2 = pd.DataFrame(device_generator)
    file_path = TARGET_DIR / "devices.csv"
    df2.to_csv(file_path, index=False)





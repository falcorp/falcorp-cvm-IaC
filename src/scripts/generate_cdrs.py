import random

import numpy as np
import pandas as pd
from pathlib import Path
import os
import sys



sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules.customer import Customer, CustomerDevice
from  modules.cdr import CallDetailRecordFactory
from modules.device import Device

if __name__ == "__main__":
    SCRIPT_DIR = Path(__file__).resolve().parent
    TARGET_DIR = SCRIPT_DIR.parent.parent / "data" / "cdrs"
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    SEED = 42

    cdr_factory = CallDetailRecordFactory(seed=SEED)

    # get devices data
    customer_file_path = SCRIPT_DIR.parent.parent / "data" / "devices" / "devices.csv"
    df = pd.read_csv(customer_file_path)
    df = df.astype(object).replace({np.nan: None})
    # get unique customer ids
    customer_ids = df["customer_id"].unique().tolist()
    cdr_records_output = []
    # expensive
    for customer_id in customer_ids:
        # create device/customer data
        for row in df.loc[df["customer_id"] == customer_id].to_dict(orient="records"):
            customer_device  = CustomerDevice(**row)
            cdr_records = cdr_factory.generate_call_detail_record(customer=customer_device)
            cdr_records_output.extend(cdr_records)
    df2 = pd.DataFrame(cdr_records_output)
    file_path = TARGET_DIR / "cdrs.csv"
    df2.to_csv(file_path, index=False)
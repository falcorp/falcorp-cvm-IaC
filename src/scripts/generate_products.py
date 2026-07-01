import random

import pandas as pd
from pathlib import Path
import os
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from modules.product import ProductFactory

if __name__ == "__main__":

    SCRIPT_DIR = Path(__file__).resolve().parent
    TARGET_DIR = SCRIPT_DIR.parent.parent / "data" / "products"
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    SEED = 42
    number_of_products = 5
    product_factory = ProductFactory(seed=SEED)
    product_generator = (product_factory.generate_product() for _ in range(number_of_products))

    df = pd.DataFrame(product_generator)
    file_path = TARGET_DIR / "products.csv"
    df.to_csv(file_path, index=False)
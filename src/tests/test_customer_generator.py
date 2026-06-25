import pytest
from pathlib import Path
import os
import sys
from datetime import datetime

from modules.customer import CustomerFactory

# Define temporary test path 
TEST_OUTPUT_PATH = "../../data/test_customer_mock_data.csv"

@pytest.fixture(autouse=True)
def cleanup_test_files():
    yield
    if os.path.exists(TEST_OUTPUT_PATH):
        os.remove(TEST_OUTPUT_PATH)

@pytest.fixture(scope="class")
def class_scoped_customer():
    return CustomerFactory(seed=40).generate_customer()

class TestCustomerCreation:

    def test_customer_attributes(self, class_scoped_customer):
        expected_attributes = [
            "customer_id", "registration_date", "termination_date",
            "date_of_birth", "gender", "signup_channel", 
            "signup_promo_code", "ported_in_status",
            "previous_carrier", "plan_id",
            "boyd", "registration_device_tac",
            "payment_method"
        ]
        
        assert expected_attributes == list(class_scoped_customer.keys())

    def test_customer_registration_date(self, class_scoped_customer):

        def convert_iso_to_date(target_iso):
            try:
                clean_iso = target_iso.replace("Z", "+00.00")
                target_datetime = datetime.fromisoformat(clean_iso)
                return target_datetime.date()
            except ValueError as e:
                print(f"Invalid ISO 8601 format: {e}")
                return None
        registration_date = class_scoped_customer.get("registration_date")
        start = datetime(2020,1,1).date()
        end = datetime.now().date()

        assert start <= convert_iso_to_date(registration_date) <= end

def test_generate_to_csv_creates_files():
    pass

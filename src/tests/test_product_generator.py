import pytest
from pathlib import Path
import os
import sys
from datetime import datetime

from modules.product import ProductFactory

@pytest.fixture(scope="class")
def class_scoped_product():
    return ProductFactory(seed=40).generate_product()

class TestCustomerCreation:

    def test_product_attributes(self, class_scoped_product):
        expected_attribtues = [
            "product_id", "product_name", "product_type",
            "billing_type", "product_price", "data_gb_allowance",
            "voice_minutes_allowance", "sms_count_allowance"
        ]
        assert expected_attribtues == list(class_scoped_product.keys())
    
    def test_product_name(self, class_scoped_product):
        allowable_product_names = [
            "TikTok & Chill Starter", "Social Storm Unlimited",
            "The Infinite Scroll", "Ping Master Elite",
            "Light & Easy Monthly", "The Keep-In-Touch Plan"
        ]

        assert class_scoped_product.get("product_name") in allowable_product_names
    
    def test_product_type(self, class_scoped_product):
        allowable_product_types = [
            "BASE_PLAN", "DATA_ADDON", "ROAMING_PASS", "VOICE_ADDON", "SMS_ADDON"
        ]
        assert class_scoped_product.get("product_type") in allowable_product_types
    
    def test_billing_type(self, class_scoped_product):
        allowable_billing_types = [
            "Postpaid", "Prepaid"
        ]

        assert class_scoped_product.get("billing_type") in allowable_billing_types
    
    def test_product_price(self, class_scoped_product):
        allowable_product_prices = [
           -1, 30, 45, 99, 50, 99, 149 
        ]
        assert class_scoped_product.get("product_price") in allowable_product_prices
    
    def test_data_gb_allowance(self, class_scoped_product):
        allowable_gb_allowance = [
            -1, 0, 1, 2, 3, 5, 8, 13, 21
        ]
        assert class_scoped_product.get("data_gb_allowance") in allowable_gb_allowance
    
    def test_voice_minutes_allowance(self, class_scoped_product):
        allowable_voice_minutes = [
           -1, 0, 5, 10, 15, 25, 40, 65, 105, 170 
        ]
        assert class_scoped_product.get("voice_minutes_allowance") in allowable_voice_minutes
    
    def test_sms_count_allowance(self, class_scoped_product):
        allowable_sms_count = [
            -1, 0, 10, 30, 40, 70, 110
        ]
        assert class_scoped_product.get("sms_count_allowance") in allowable_sms_count
    
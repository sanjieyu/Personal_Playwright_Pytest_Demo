# Author:Yi Sun(Tim) 2024-1-22

import pytest
import os
from utils.read_config import ReadConfig

@pytest.fixture(scope="session")
def config_reader():
    return ReadConfig()

@pytest.fixture(scope="session")
def credentials(config_reader):
    """Get the credential from config_reader"""
    return {
        "egd_url": config_reader.get_url(),
        "admin_username": config_reader.admin_username(),
        "admin_password": config_reader.admin_password(),
        "dealer_username": config_reader.dealer_username(),
        "dealer_password": config_reader.dealer_password(),
        "sales_username": config_reader.sales_username(),
        "sales_password": config_reader.sales_password()
    }

@pytest.fixture(scope="session")
def auth_files():
    """auth file for different roles"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return {
        "admin": os.path.join(root_dir,"auth_admin.json"),
        "dealer": os.path.join(root_dir,"auth_dealer.json"),
        "sales": os.path.join(root_dir,"auth_sales.json")
    }

@pytest.fixture(scope="session")
def base_url(credentials):
    return credentials["egd_url"]



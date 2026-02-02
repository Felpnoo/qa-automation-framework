import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_success(page: Page):
    # 1. Arrange
    login_p = LoginPage(page)
    inventory_p = InventoryPage(page)
    
    # 2. Act
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")
    
    # 3. Assert
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    assert inventory_p.get_header() == "Products"

def test_login_invalid_user(page: Page):
    login_p = LoginPage(page)
    
    login_p.navigate()
    login_p.login("locked_out_user", "secret_sauce")
    
    assert "Epic sadface" in login_p.get_error_message()

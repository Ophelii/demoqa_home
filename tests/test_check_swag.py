from pages.swag_labs import SwagLabs
from conftest import browser


def test_icon(browser):
    swag_lab_icon = SwagLabs(browser)
    swag_lab_icon.visit()
    assert swag_lab_icon.exist_icon()

def test_name_field(browser):
    swag_lab_name = SwagLabs(browser)
    swag_lab_name.visit()
    assert swag_lab_name.name_field_exist()


def test_password_field(browser):
    swag_lab_password = SwagLabs(browser)
    swag_lab_password.visit()
    assert swag_lab_password.password_field_exist()

from tests.helpers.support_functions import *
from tests.page_object import add_invoice
from config import test_settings

invoice_status = '//*[@id="messages-panel-header"]/div/app-enum/div/span[1]'
create_correction_button = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-details/div/div[1]/div/div/div[1]/div'
invoice_is_SP = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-details/div/div[1]/div/div/section[1]/ul/li'
invoice_number = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-details/div/div[1]/div/div/section[1]/div'
invoice_gross_amount = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-details/div/div[1]/div/div/section[2]/div[2]/div[2]/div[1]/ul/li[1]/span'
invoice_net_amount = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-details/div/div[1]/div/div/section[2]/div[2]/div[2]/div[1]/ul/li[2]/span'
invoice_vat_amount = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-details/div/div[1]/div/div/section[2]/div[2]/div[2]/div[1]/ul/li[3]/span'


def wait_for_invoice_view(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, create_correction_button, 30)
    return elem.is_displayed()


def check_invoice_status(driver_instance):
    elem = driver_instance.find_element(By.XPATH, invoice_status)
    print(elem.text)
    if elem.text == 'ZGŁOSZONA':
        return True
    else:
        return False


def check_invoice_is_sp(driver_instance):
    elem = driver_instance.find_element(By.XPATH, invoice_is_SP)
    print(elem.text)
    if elem.text == 'Bez Split Payment':
        return False
    elif elem.text == 'Split Payment':
        return True


def check_invoice_gross_amount(driver_instance, gross_amount):
    elem = driver_instance.find_element(By.XPATH, invoice_gross_amount)
    print(elem.text)
    if get_amount_from_string(elem.text) == gross_amount:
        return True
    else:
        return False


def check_invoice_net_amount(driver_instance, gross_amount, vat_amount):
    elem = driver_instance.find_element(By.XPATH, invoice_net_amount)
    calculated_net_amount = str(float(gross_amount.replace(',', '.')) - float(vat_amount.replace(',', '.'))).replace('.', ',')
    if get_amount_from_string(elem.text) == calculated_net_amount:
        return True
    else:
        return False


def check_invoice_vat_amount(driver_instance, vat_amount):
    elem = driver_instance.find_element(By.XPATH, invoice_vat_amount)
    if get_amount_from_string(elem.text) == vat_amount:
        return True
    else:
        return False

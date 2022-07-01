from tests.helpers.support_functions import *
from config import test_settings
from time import sleep

invoices_content = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/div[1]/h1'
search_input = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/input'
# /html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/input
search_button = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/div/button'
search_result = '//table/tbody/tr/td[2]'
search_result_row = '//table/tbody/tr'
# search_result = '/html/body/app-root/app-layout/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[2]/app-link-column/a/span[2]'
add_invoice_button = '/html/body/app-root/app-layout-authenticated/div/app-header/div/div[2]/app-add-invoice-button/div/button'

search_result_invoice_number = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[2]'
search_result_contractor = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[3]'
search_result_sale_date = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[4]'
search_result_sale_date_class = 'cell.column-date'
search_result_date_of_payment = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[5]'
search_result_gross_amount = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[6]'
search_result_advance_payment = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[7]'
search_result_debtor_balance = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[8]'
search_result_risk_acceptance = ''
search_result_status = '/html/body/app-root/app-layout-authenticated/main/div/app-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[10]'


def invoices_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, invoices_content)
    return elem.is_displayed()


def search_invoice(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, search_button)
    elem = driver_instance.find_element(By.XPATH, search_input)
    elem.send_keys(test_settings.documents.invoice)
    elem1 = driver_instance.find_element(By.XPATH, search_button)
    elem1.click()
    sleep(1)


def open_add_invoice_popup(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, add_invoice_button)
    elem = driver_instance.find_element(By.XPATH, add_invoice_button)
    elem.click()


def check_invoice_number_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_invoice_number)
    if elem.text == test_settings.documents.invoice:
        return True
    else:
        return False


def check_contractor_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_contractor)
    if test_settings.documents.contractor in elem.text:
        return True
    else:
        return False


def check_sale_date_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_sale_date)
    return elem.is_displayed()


def check_date_of_pay_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_date_of_payment)
    return elem.is_displayed()


def check_gross_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_gross_amount)
    return elem.is_displayed()


def check_advance_payment_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_advance_payment)
    return elem.is_displayed()


def check_debtor_balance_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_debtor_balance)
    return elem.is_displayed()


def check_status_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_status)
    return elem.is_displayed()
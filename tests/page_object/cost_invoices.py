from tests.helpers.support_functions import *
from config import test_settings

search_input = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/input'
search_button = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/div/button'
search_result_cost_invoice_number = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[2]/app-link-column/a'
search_result_type = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[3]'
search_result_sale_date = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[5]'
search_result_date_of_payment = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[6]'
search_result_amount = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[7]'
search_result_remaining_amount_to_pay = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[8]'
search_result_status = '/html/body/app-root/app-layout-authenticated/main/div/app-cost-invoice-list/app-base-list/app-generic-table/table/tbody/tr/td[9]'


def search_cost_invoice(driver_instance):
    elem = driver_instance.find_element(By.XPATH, search_input)
    elem.send_keys(test_settings.documents.cost_invoice)
    elem1 = driver_instance.find_element(By.XPATH, search_button)
    elem1.click()


def check_cost_invoice_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_cost_invoice_number)
    if elem.text == test_settings.documents.cost_invoice:
        return True
    else:
        return False


def check_type_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_type)
    return elem.is_displayed()


def check_sale_date_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_sale_date)
    return elem.is_displayed()


def check_date_of_payment_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_date_of_payment)
    return elem.is_displayed()


def check_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_amount)
    return elem.is_displayed()


def check_remaining_amount_to_pay_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_remaining_amount_to_pay)
    return elem.is_displayed()


def check_status_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_status)
    return elem.is_displayed()

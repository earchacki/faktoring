from tests.helpers.support_functions import *
from config import test_settings
from time import sleep

search_input = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/input'
search_button = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/div/button'
search_result_payment = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/app-generic-table/table/tbody/tr/td[2]'
search_result_type = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/app-generic-table/table/tbody/tr/td[3]/app-enum-column'
search_result_payment_date = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/app-generic-table/table/tbody/tr/td[4]/app-date-column'
search_result_amount = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/app-generic-table/table/tbody/tr/td[5]/app-currency-column'
search_result_deduction_amount = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/app-generic-table/table/tbody/tr/td[6]/app-currency-column'
search_result_transaction_amount = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/app-generic-table/table/tbody/tr/td[7]/app-currency-column'
search_result_title = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/app-generic-table/table/tbody/tr/td[8]/app-text-column'


def search_payment(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_input)
    elem.send_keys(test_settings.documents.payment)
    elem1 = driver_instance.find_element(By.XPATH, search_button)
    elem1.click()
    sleep(1)


def check_payment_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_payment)
    if test_settings.documents.payment in elem.text:
        return True
    else:
        return False


def check_type_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_type)
    return elem.is_displayed()


def check_payment_date_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_payment_date)
    return elem.is_displayed()


def check_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_amount)
    return elem.is_displayed()


def check_deduction_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_deduction_amount)
    return elem.is_displayed()


def check_transaction_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_transaction_amount)
    return elem.is_displayed()


def check_title_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_title)
    return elem.is_displayed()




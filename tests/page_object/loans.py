from tests.helpers.support_functions import *
from config import test_settings
from time import sleep

search_input = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/input'
search_button = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/div/button'
search_result_loan = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/app-generic-table/table/tbody/tr/td[2]/app-link-column'
search_result_issue_date = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/app-generic-table/table/tbody/tr/td[3]/app-date-column'
search_result_payment_date = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/app-generic-table/table/tbody/tr/td[4]/app-date-column'
search_result_amount = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/app-generic-table/table/tbody/tr/td[5]/app-currency-column'
search_result_commission_amount = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/app-generic-table/table/tbody/tr/td[6]/app-currency-column'
search_result_balance = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/app-generic-table/table/tbody/tr/td[7]/app-currency-column'
search_result_status = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/app-generic-table/table/tbody/tr/td[8]/app-enum-column'


def search_loan(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_input)
    elem.send_keys(test_settings.documents.loan)
    elem1 = driver_instance.find_element(By.XPATH, search_button)
    elem1.click()
    sleep(1)


def check_loan_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_loan)
    if test_settings.documents.loan in elem.text:
        return True
    else:
        return False


def check_issue_date_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_issue_date)
    return elem.is_displayed()


def check_payment_date_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_payment_date)
    return elem.is_displayed()


def check_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_amount)
    return elem.is_displayed()


def check_commission_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_commission_amount)
    return elem.is_displayed()


def check_balance_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_balance)
    return elem.is_displayed()


def check_status_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_status)
    return elem.is_displayed()

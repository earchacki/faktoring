from tests.helpers.support_functions import *
from config import test_settings
from time import sleep

search_input = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/input'
search_button = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/div'
search_result_repayments_id = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/app-generic-table/table/tbody/tr/td[2]'
search_result_payer = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/app-generic-table/table/tbody/tr/td[3]'
search_result_repayment_date = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/app-generic-table/table/tbody/tr/td[4]'
search_result_amount = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/app-generic-table/table/tbody/tr/td[5]'
search_result_settled_amount = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/app-generic-table/table/tbody/tr/td[6]'
search_result_left_to_settled_amount = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/app-generic-table/table/tbody/tr/td[7]'
search_result_details = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/app-generic-table/table/tbody/tr/td[8]'
search_result_status = '/html/body/app-root/app-layout-authenticated/main/div/app-repayment-list/app-base-list/app-generic-table/table/tbody/tr/td[9]'


def search_repayment(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_input)
    elem.send_keys(test_settings.documents.repayment)
    elem1 = driver_instance.find_element(By.XPATH, search_button)
    elem1.click()
    sleep(1)


def check_repayment_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_repayments_id)
    if test_settings.documents.repayment in elem.text:
        return True
    else:
        return False


def check_payer_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_payer)
    if test_settings.documents.contractor in elem.text:
        return True
    else:
        return False


def check_repayment_date_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_repayment_date)
    return elem.is_displayed()


def check_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_amount)
    return elem.is_displayed()


def check_left_to_settled_amount_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_left_to_settled_amount)
    return elem.is_displayed()


def check_details_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_details)
    return elem.is_displayed()


def check_status_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_status)
    return elem.is_displayed()

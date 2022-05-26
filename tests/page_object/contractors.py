from tests.helpers.support_functions import *
from tests.page_object import main_page
from config import test_settings
from time import sleep

search_input = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/input'
search_button = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/div[2]/div/app-base-filter-inline/div/div/div[1]/div/button'
search_result_contractor = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/app-generic-table/table/tbody/tr/td[2]/app-text-column/div/div'
search_result_limit = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/app-generic-table/table/tbody/tr/td[3]/app-currency-column/div'
search_result_current_financing = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/app-generic-table/table/tbody/tr/td[4]/app-currency-column/div'
search_result_available_limit = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/app-generic-table/table/tbody/tr/td[5]/app-currency-column/div'
search_result_financig_level = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/app-generic-table/table/tbody/tr/td[6]/app-text-column/div/div'
# search_result_risk = ''
search_result_status = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/app-generic-table/table/tbody/tr/td[8]/app-enum-column/app-enum/div/span[1]'


def search_contractor(driver_instance):
    elem = driver_instance.find_element(By.XPATH, search_input)
    elem.send_keys(test_settings.documents.contractor)
    elem1 = driver_instance.find_element(By.XPATH, search_button)
    elem1.click()
    sleep(1)


def check_contractor_visible(driver_instance):
    elem = driver_instance.find_element(By.XPATH, search_result_contractor)
    print(elem.text)
    if test_settings.documents.contractor in elem.text:
        return True
    else:
        return False


def check_limit_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_limit)
    return elem.is_displayed()


def check_current_financing_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_current_financing)
    return elem.is_displayed()


def check_available_limit_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_available_limit)
    return elem.is_displayed()


def check_financing_level_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_financig_level)
    return elem.is_displayed()


def check_status_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, search_result_status)
    return elem.is_displayed()



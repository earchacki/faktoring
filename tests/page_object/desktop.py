from tests.helpers.support_functions import *
from tests.page_object import main_page

available_limit = '/html/body/app-root/app-layout-authenticated/main/div/app-dashboard/div/div/div[1]/app-dashboard-limit/div/div/div[2]/span'
small_available_limit = '/html/body/app-root/app-layout-authenticated/main/div/app-dashboard/div/div/div[1]/app-dashboard-limit/div/div/div[4]/div[2]/div[1]/span'
current_financing = '/html/body/app-root/app-layout-authenticated/main/div/app-dashboard/div/div/div[1]/app-dashboard-limit/div/div/div[4]/div[2]/div[2]/span'
change_limit_button = '//button[text() = "Zwiększ limit"]'
change_limit_label = '/html/body/ngb-modal-window/div/div/app-simple-dialog/div[1]/h4'


def available_limit_is_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, available_limit)
    return elem.is_displayed()


def small_available_limit_is_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, small_available_limit)
    return elem.is_displayed()


def current_financing_is_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, current_financing)
    return elem.is_displayed()


def change_limit(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, change_limit_button)
    elem.click()
    elem1 = wait_for_visibility_of_element(driver_instance, By.XPATH, change_limit_label)
    if elem1.text == 'Skontaktuj się z opiekunem':
        return True
    else:
        return False





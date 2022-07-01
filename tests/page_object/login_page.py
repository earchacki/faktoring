from tests.helpers.support_functions import *
from tests.page_object.invoices import invoices_content_visible
from config import test_settings

login_page_header = '/html/head/title'
login_page_content = '/html/body/app-root/app-login/app-layout-general/main/div/div/div[1]/div/div/div'
input_login = 'userName'
input_password = 'password'
button_login = '/html/body/app-root/app-login/app-layout-general/main/div/div/div[1]/div/div/form/button'


def content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, login_page_content)
    return elem.is_displayed()


def login_correct(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, login_page_content)
    elem = driver_instance.find_element(By.ID, input_login)
    elem.send_keys(test_settings.environment.login)
    elem1 = driver_instance.find_element(By.ID, input_password)
    elem1.send_keys(test_settings.environment.password)
    elem2 = driver_instance.find_element(By.XPATH, button_login )
    elem2.click()
    return invoices_content_visible(driver_instance)

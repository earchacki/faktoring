from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from datetime import datetime
import pymssql
from config import test_settings


# funkcja najeżdza na element, aż się rozwinie zawartość na skutek najechania
def hover_over_element(driver_instance, selector_type, selector):
    elem = driver_instance.find_element(selector_type, selector)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def wait_for_visibility_of_element(driver_instance, selector_type, selector, time_to_wait=5):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((selector_type, selector)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element(inv_driver_instance, selector_type, selector, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((selector_type, selector)))
    return inv_elem


def check_if_element_is_no_clickable(driver_instance, selector_type, selector, time_to_wait=8):
    elem = WebDriverWait(driver_instance, time_to_wait).until_not(EC.element_to_be_clickable((selector_type, selector)))
    return elem

# do sprawdzenia jak będzie działać, bo nieużywana jeszcze
def get_dropdown_value(driver_instance, selector_type, selector, selected_value):
    elem_list = Select(driver_instance.find_element(selector_type, selector))
    #wait_for_visibility_of_element(driver_instance, selector_type, selector)
    elem_list.select_by_value(selected_value)
    return elem_list


def generate_invoice_number():
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    invoice_number = 'FV' + now
    return invoice_number


def get_amount_from_string(string):
    amount = ''
    for i in string:
        if i.isdigit():
            amount = amount + i
        elif i == ',':
            amount = amount + i
    return amount


def get_system_date():
    conn = pymssql.connect(test_settings.environment.db_server, test_settings.environment.db_login,
                           test_settings.environment.db_password, test_settings.environment.db_name)
    cursor = conn.cursor()
    sql_query = 'select system_date as system_iso_date, dateadd(d,14, system_date) as payment_iso_date from dbo.config'
    cursor.execute(sql_query)
    sql_results = (cursor.fetchall())
    sale_date = sql_results[0][0].strftime('%d-%m-%Y')
    payment_date = sql_results[0][1].strftime('%d-%m-%Y')
    return sale_date, payment_date

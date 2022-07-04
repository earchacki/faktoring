from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from config import test_settings


input_contractor = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[2]/app-invoice-contractor-lookup/ng-select/div/div/div[2]/input'
input_invoice_no = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[3]/input'
input_sale_date = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[4]/div[1]/app-date-input/input'
input_payment_date = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[4]/div[2]/app-date-input/input'
input_amount_gross = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[5]/div[1]/div/app-decimal-input/input'
input_amount_vat = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[6]/div[1]/div/app-decimal-input/input'
add_invoice_button = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[3]/button[2]'
no_Vat_checkbox = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[5]/div[2]/app-checkbox/label'
is_Sp_checkbox = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[6]/div[2]/app-checkbox/label'
currency_button = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[5]/div[1]/div/app-decimal-input/div'
change_currency_button = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[5]/div[1]/div/app-decimal-input/div/div/button[2]'
input_amount_vat_in_pln = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[7]/div/div/app-decimal-input/input'
invoice_to_financing = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[1]/app-radio-buttons/div/div[1]/label'
invoice_to_administraction = '/html/body/ngb-modal-window/div/div/app-new-invoice/form/div[2]/div[1]/app-radio-buttons/div/div[2]/label'

contractor_name = 'F.H.U. FOLPAK'
sale_date = get_system_date()[0]
payment_date = get_system_date()[1]


def set_invoice_to_financing(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, invoice_to_financing)
    elem.click()


def set_invoice_to_administraction(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, invoice_to_administraction)
    elem.click()


def add_contractor(driver_instance):
    wait_for_visibility_of_element(driver_instance, By.XPATH, input_contractor)
    elem = driver_instance.find_element(By.XPATH, input_contractor)
    elem.click()
    elem.send_keys(test_settings.documents.contractor)
    elem.send_keys(Keys.ENTER)


def add_invoice_no(driver_instance):
    elem = driver_instance.find_element(By.XPATH, input_invoice_no)
    invoice_number = generate_invoice_number()
    elem.send_keys(invoice_number)
    return invoice_number


def add_sale_date(driver_instance):
    elem = driver_instance.find_element(By.XPATH, input_sale_date)
    elem.send_keys(sale_date)


def add_payment_date(driver_instance):
    elem = driver_instance.find_element(By.XPATH, input_payment_date)
    elem.send_keys(payment_date)


def add_amount_gross(driver_instance, gross_amount):
    elem = driver_instance.find_element(By.XPATH, input_amount_gross)
    elem.send_keys(gross_amount)


def add_amount_vat(driver_instance, vat_amount):
    elem = driver_instance.find_element(By.XPATH, input_amount_vat)
    elem.send_keys(vat_amount)


def add_amount_vat_in_pln(driver_instance, vat_in_pln_amount):
    elem = driver_instance.find_element(By.XPATH, input_amount_vat_in_pln)
    elem.send_keys(vat_in_pln_amount)


def change_currency(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, By.XPATH, currency_button)
    elem.click()
    try:
        elem1 = driver_instance.find_element(By.XPATH, change_currency_button)
        elem1.click()
    except NoSuchElementException:
        print('Do wyboru możliwa tylko jedna waluta')
        return True


def add_amount_vat_is_block(driver_instance, value):
    elem = check_if_input_is_block(driver_instance, By.XPATH, input_amount_vat, value)
    return elem


def click_no_vat_checkbox(driver_instance):
    elem = driver_instance.find_element(By.XPATH, no_Vat_checkbox)
    elem.click()


def click_is_sp_checkbox(driver_instance):
    elem = driver_instance.find_element(By.XPATH, is_Sp_checkbox)
    elem.click()


def fill_all_fields_invoice_pln(driver_instance):
    add_contractor(driver_instance)
    add_invoice_no(driver_instance)
    add_sale_date(driver_instance)
    add_payment_date(driver_instance)
    add_amount_gross(driver_instance, test_settings.invoice_vat.gross_amount)
    add_amount_vat(driver_instance, test_settings.invoice_vat.vat_amount)


def fill_all_fields_invoice_pln_no_vat(driver_instance):
    add_contractor(driver_instance)
    add_invoice_no(driver_instance)
    add_sale_date(driver_instance)
    add_payment_date(driver_instance)
    add_amount_gross(driver_instance, test_settings.invoice_no_vat.gross_amount)
    click_no_vat_checkbox(driver_instance)
    add_amount_vat_is_block(driver_instance, test_settings.invoice_vat.vat_amount)


def fill_all_fields_invoice_pln_is_sp(driver_instance):
    add_contractor(driver_instance)
    add_invoice_no(driver_instance)
    add_sale_date(driver_instance)
    add_payment_date(driver_instance)
    add_amount_gross(driver_instance, test_settings.invoice_is_sp.gross_amount)
    add_amount_vat(driver_instance, test_settings.invoice_is_sp.vat_amount)
    click_is_sp_checkbox(driver_instance)


def fill_all_fields_invoice_eur(driver_instance):
    add_contractor(driver_instance)
    add_invoice_no(driver_instance)
    add_sale_date(driver_instance)
    add_payment_date(driver_instance)
    change_currency(driver_instance)
    add_amount_gross(driver_instance, test_settings.invoice_vat.gross_amount)
    add_amount_vat(driver_instance, test_settings.invoice_vat.vat_amount)


def fill_all_fields_invoice_EUR_is_SP(driver_instance):
    add_contractor(driver_instance)
    add_invoice_no(driver_instance)
    add_sale_date(driver_instance)
    add_payment_date(driver_instance)
    change_currency(driver_instance)
    add_amount_gross(driver_instance, test_settings.invoice_is_sp_eur.gross_amount)
    add_amount_vat(driver_instance, test_settings.invoice_is_sp_eur.vat_amount)
    click_is_sp_checkbox(driver_instance)
    add_amount_vat_in_pln(driver_instance, test_settings.invoice_is_sp_eur.vat_in_pln_amount)


def fill_all_fields_invoice_eur_not_possible(driver_instance):
    add_contractor(driver_instance)
    add_invoice_no(driver_instance)
    add_sale_date(driver_instance)
    add_payment_date(driver_instance)
    add_amount_gross(driver_instance, test_settings.invoice_vat.gross_amount)
    add_amount_vat(driver_instance, test_settings.invoice_vat.vat_amount)


def submit_invoice(driver_instance):
    wait_if_button_is_disable(driver_instance, By.XPATH, add_invoice_button)
    elem = driver_instance.find_element(By.XPATH, add_invoice_button)
    elem.click()


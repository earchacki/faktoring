from tests.helpers.support_functions import *

desktop_tab_link = '/html/body/app-root/app-layout/div/app-navbar/div/ul/li[1]/a'
desktop_tab_header = '/html/body/app-root/app-layout/main/div/app-dashboard/div/div/div[1]/app-dashboard-limit/div/div/div[1]/span'
invoices_tab_link = '/html/body/app-root/app-layout/div/app-navbar/div/ul/li[2]'
invoices_tab_header = '/html/body/app-root/app-layout/main/div/app-invoice-list/app-base-list/div[1]/h1'
contractors_tab_link = '/html/body/app-root/app-layout/div/app-navbar/div/ul/li[3]/a'
contractors_tab_header = '/html/body/app-root/app-layout/main/div/app-contractor-list/app-base-list/div[1]/h1'
cost_invoices_tab_link = '/html/body/app-root/app-layout/div/app-navbar/div/ul/li[4]/a'
cost_invoices_header = '/html/body/app-root/app-layout/main/div/app-cost-invoice-list/app-base-list/div[1]/h1'
repayments_tab_link = '/html/body/app-root/app-layout/div/app-navbar/div/ul/li[5]/a'
repayments_tab_header = '/html/body/app-root/app-layout/main/div/app-repayment-list/app-base-list/div[1]/h1'
payments_tab_link = '/html/body/app-root/app-layout/div/app-navbar/div/ul/li[6]/a'
payments_tab_header = '/html/body/app-root/app-layout/main/div/app-payment-list/app-base-list/div[1]/h1'
loans_tab_link = '/html/body/app-root/app-layout/div/app-navbar/div/ul/li[7]/a'
loans_tab_header = '/html/body/app-root/app-layout/main/div/app-loan-list/app-base-list/div[1]/h1'


def go_desktop_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, desktop_tab_link)
    elem.click()
    elem1 = wait_for_visibility_of_element(driver_instance, By.XPATH, desktop_tab_header)
    if elem1.text == 'Dostępne finansowanie':
        return True
    else:
        return False


def go_invoices_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, invoices_tab_link)
    elem.click()
    elem1 = wait_for_visibility_of_element(driver_instance, By.XPATH, invoices_tab_header)
    if elem1.text == 'Faktury':
        return True
    else:
        return False


def go_contractors_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, contractors_tab_link)
    elem.click()
    elem1 = wait_for_visibility_of_element(driver_instance, By.XPATH, contractors_tab_header)
    print(elem1.text)
    if elem1.text == 'Kontrahenci':
        return True
    else:
        return False


def go_cost_invoices_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, cost_invoices_tab_link)
    elem.click()
    elem1 = wait_for_visibility_of_element(driver_instance, By.XPATH, cost_invoices_header)
    if elem1.text == 'Opłaty i prowizje':
        return True
    else:
        return False


def go_repayments_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, repayments_tab_link)
    elem.click()
    elem1 = wait_for_visibility_of_element(driver_instance, By.XPATH, repayments_tab_header)
    if elem1.text == 'Spłaty':
        return True
    else:
        return False


def go_payments_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, payments_tab_link)
    elem.click()
    elem1 = wait_for_visibility_of_element(driver_instance, By.XPATH, payments_tab_header)
    if elem1.text == 'Wypłaty':
        return True
    else:
        return False


def go_loans_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, loans_tab_link)
    elem.click()
    elem1 = wait_for_visibility_of_element(driver_instance, By.XPATH, loans_tab_header)
    if elem1.text == 'Lista pożyczek na klik':
        return True
    else:
        return False


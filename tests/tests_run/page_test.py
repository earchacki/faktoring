import unittest
from selenium import webdriver
# from config.test_settings import TestSettings
from tests.page_object import login_page, invoices, add_invoice, invoice_details, main_page, desktop, contractors, cost_invoices, repayments, payments, loans
# from tests.tests_data import tests_data
from config import test_settings
from time import sleep
import sys
import os


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.url = tests_data.environment_rc.page_url
        self.url = test_settings.environment.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test01_login_page_content_visible(self):
        self.assertTrue(login_page.content_visible(self.driver))

    def test02_login_page_correct_login(self):
        self.assertTrue(login_page.login_correct(self.driver))

    def test03_check_invoices_tab_content(self):
        login_page.login_correct(self.driver)
        self.assertTrue(main_page.go_invoices_tab(self.driver))
        invoices.search_invoice(self.driver)
        self.assertTrue(invoices.check_invoice_number_visible(self.driver))
        self.assertTrue(invoices.check_contractor_visible(self.driver))
        self.assertTrue(invoices.check_sale_date_visible(self.driver))
        self.assertTrue(invoices.check_date_of_pay_visible(self.driver))
        self.assertTrue(invoices.check_gross_amount_visible(self.driver))
        self.assertTrue(invoices.check_advance_payment_visible(self.driver))
        self.assertTrue(invoices.check_debtor_balance_visible(self.driver))
        self.assertTrue(invoices.check_status_visible(self.driver))

    def test04_add_invoice(self):
        login_page.login_correct(self.driver)
        invoices.open_add_invoice_popup(self.driver)
        add_invoice.fill_all_fields_invoice_pln(self.driver)
        add_invoice.submit_invoice(self.driver)
        self.assertTrue(invoice_details.wait_for_invoice_view(self.driver))
        self.assertTrue(invoice_details.check_invoice_status(self.driver))
        self.assertFalse(invoice_details.check_invoice_is_sp(self.driver))
        self.assertTrue(invoice_details.check_invoice_gross_amount(self.driver, test_settings.invoice_vat.gross_amount))
        self.assertTrue((invoice_details.check_invoice_net_amount(self.driver, test_settings.invoice_vat.gross_amount, test_settings.invoice_vat.vat_amount)))
        self.assertTrue(invoice_details.check_invoice_vat_amount(self.driver, test_settings.invoice_vat.vat_amount))

    def test05_add_invoice_no_vat(self):
        login_page.login_correct(self.driver)
        invoices.open_add_invoice_popup(self.driver)
        add_invoice.fill_all_fields_invoice_pln_no_vat(self.driver)
        self.assertTrue(add_invoice.add_amount_vat_is_block(self.driver, test_settings.invoice_vat.vat_amount))
        add_invoice.submit_invoice(self.driver)
        self.assertTrue(invoice_details.wait_for_invoice_view(self.driver))
        self.assertTrue(invoice_details.check_invoice_status(self.driver))
        self.assertFalse(invoice_details.check_invoice_is_sp(self.driver))
        self.assertTrue(invoice_details.check_invoice_gross_amount(self.driver, test_settings.invoice_no_vat.gross_amount))

    def test06_add_invoice_is_sp(self):
        login_page.login_correct(self.driver)
        invoices.open_add_invoice_popup(self.driver)
        add_invoice.fill_all_fields_invoice_pln_is_sp(self.driver)
        add_invoice.submit_invoice(self.driver)
        self.assertTrue(invoice_details.wait_for_invoice_view(self.driver))
        self.assertTrue(invoice_details.check_invoice_status(self.driver))
        self.assertTrue(invoice_details.check_invoice_is_sp(self.driver))
        self.assertTrue(invoice_details.check_invoice_gross_amount(self.driver, test_settings.invoice_no_vat.gross_amount))
        self.assertTrue(invoice_details.check_invoice_net_amount(self.driver, test_settings.invoice_is_sp.gross_amount, test_settings.invoice_is_sp.vat_amount))
        self.assertTrue(invoice_details.check_invoice_vat_amount(self.driver, test_settings.invoice_is_sp.vat_amount))

    def test07_add_invoice_in_eur(self):
        login_page.login_correct(self.driver)
        invoices.open_add_invoice_popup(self.driver)
        add_invoice.fill_all_fields_invoice_eur(self.driver)
        add_invoice.submit_invoice(self.driver)
        self.assertTrue(invoice_details.wait_for_invoice_view(self.driver))
        self.assertTrue(invoice_details.check_invoice_status(self.driver))
        self.assertFalse(invoice_details.check_invoice_is_sp(self.driver))
        self.assertTrue(invoice_details.check_invoice_gross_amount(self.driver, test_settings.invoice_vat.gross_amount))
        self.assertTrue(invoice_details.check_invoice_net_amount(self.driver, test_settings.invoice_vat.gross_amount, test_settings.invoice_vat.vat_amount))
        self.assertTrue(invoice_details.check_invoice_vat_amount(self.driver, test_settings.invoice_vat.vat_amount))

    def test08_add_invoice_in_eur_is_sp(self):
        login_page.login_correct(self.driver)
        invoices.open_add_invoice_popup(self.driver)
        add_invoice.fill_all_fields_invoice_EUR_is_SP(self.driver)
        add_invoice.submit_invoice(self.driver)
        self.assertTrue(invoice_details.wait_for_invoice_view(self.driver))
        self.assertTrue(invoice_details.check_invoice_status(self.driver))
        self.assertTrue(invoice_details.check_invoice_is_sp(self.driver))
        self.assertTrue(invoice_details.check_invoice_gross_amount(self.driver, test_settings.invoice_is_sp_eur.gross_amount))
        self.assertTrue(invoice_details.check_invoice_net_amount(self.driver, test_settings.invoice_is_sp_eur.gross_amount, test_settings.invoice_is_sp_eur.vat_amount))
        self.assertTrue(invoice_details.check_invoice_vat_amount(self.driver, test_settings.invoice_is_sp_eur.vat_amount))

    def test09_check_desktop_tab_content(self):
        login_page.login_correct(self.driver)
        self.assertTrue(main_page.go_desktop_tab(self.driver))
        self.assertTrue(desktop.available_limit_is_visible(self.driver))
        self.assertTrue(desktop.small_available_limit_is_visible(self.driver))
        self.assertTrue(desktop.current_financing_is_visible(self.driver))
        self.assertTrue(desktop.change_limit(self.driver))

    def test10_check_contractors_tab_content(self):
        login_page.login_correct(self.driver)
        self.assertTrue(main_page.go_contractors_tab(self.driver))
        contractors.search_contractor(self.driver)
        self.assertTrue(contractors.check_contractor_visible(self.driver))
        self.assertTrue(contractors.check_limit_visible(self.driver))
        self.assertTrue(contractors.check_current_financing_visible(self.driver))
        self.assertTrue(contractors.check_available_limit_visible(self.driver))
        self.assertTrue(contractors.check_financing_level_visible(self.driver))
        self.assertTrue(contractors.check_status_visible(self.driver))

    def test11_check_cost_invoices_tab_content(self):
        login_page.login_correct(self.driver)
        self.assertTrue(main_page.go_cost_invoices_tab(self.driver))
        cost_invoices.search_cost_invoice(self.driver)
        self.assertTrue(cost_invoices.check_cost_invoice_visible(self.driver))
        self.assertTrue(cost_invoices.check_type_visible(self.driver))
        self.assertTrue(cost_invoices.check_sale_date_visible(self.driver))
        self.assertTrue(cost_invoices.check_cost_invoice_visible(self.driver))
        self.assertTrue(cost_invoices.check_remaining_amount_to_pay_visible(self.driver))
        self.assertTrue(cost_invoices.check_amount_visible(self.driver))
        self.assertTrue(cost_invoices.check_remaining_amount_to_pay_visible(self.driver))
        self.assertTrue(cost_invoices.check_status_visible(self.driver))

    def test12_check_repayments_tab_content(self):
        login_page.login_correct(self.driver)
        self.assertTrue(main_page.go_repayments_tab(self.driver))
        repayments.search_repayment(self.driver)
        self.assertTrue(repayments.check_repayment_visible(self.driver))
        self.assertTrue(repayments.check_payer_visible(self.driver))
        self.assertTrue(repayments.check_repayment_date_visible(self.driver))
        self.assertTrue(repayments.check_amount_visible(self.driver))
        self.assertTrue(repayments.check_left_to_settled_amount_visible(self.driver))
        self.assertTrue(repayments.check_details_visible(self.driver))
        self.assertTrue(repayments.check_status_visible(self.driver))

    def test13_check_payments_tab_content(self):
        login_page.login_correct(self.driver)
        self.assertTrue(main_page.go_payments_tab(self.driver))
        payments.search_payment(self.driver)
        self.assertTrue(payments.check_payment_visible(self.driver))
        self.assertTrue(payments.check_type_visible(self.driver))
        self.assertTrue(payments.check_payment_date_visible(self.driver))
        self.assertTrue(payments.check_amount_visible(self.driver))
        self.assertTrue(payments.check_amount_visible(self.driver))
        self.assertTrue(payments.check_deduction_amount_visible(self.driver))
        self.assertTrue(payments.check_transaction_amount_visible(self.driver))
        self.assertTrue(payments.check_title_visible(self.driver))

    def test14_check_loan_tab_content(self):
        login_page.login_correct(self.driver)
        self.assertTrue(main_page.go_loans_tab(self.driver))
        loans.search_loan(self.driver)
        self.assertTrue(loans.check_loan_visible(self.driver))
        self.assertTrue(loans.check_issue_date_visible(self.driver))
        self.assertTrue(loans.check_payment_date_visible(self.driver))
        self.assertTrue(loans.check_amount_visible(self.driver))
        self.assertTrue(loans.check_commission_amount_visible(self.driver))
        self.assertTrue(loans.check_balance_visible(self.driver))
        self.assertTrue(loans.check_status_visible(self.driver))

# tutaj trzeba doda?? Umow?? bez rach. cesji w eur
#     def test15_add_invoice_in_eur_not_possible(self):
#         login_page.login_correct(self.driver)
#         invoices.open_add_invoice_popup(self.driver)
#         self.assertTrue(add_invoice.change_currency(self.driver))
#         add_invoice.fill_all_fields_invoice_eur_not_possible(self.driver)
#         add_invoice.submit_invoice(self.driver)
#         self.assertTrue(invoice_details.wait_for_invoice_view(self.driver))
#         self.assertTrue(invoice_details.check_invoice_status(self.driver))
#         self.assertFalse(invoice_details.check_invoice_is_sp(self.driver))
#         self.assertTrue(invoice_details.check_invoice_gross_amount(self.driver, test_settings.invoice_vat.gross_amount))
#         self.assertTrue(invoice_details.check_invoice_net_amount(self.driver, test_settings.invoice_vat.gross_amount, test_settings.invoice_vat.vat_amount))
#         self.assertTrue(invoice_details.check_invoice_vat_amount(self.driver, test_settings.invoice_vat.vat_amount))
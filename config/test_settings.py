import os


class TestSettings:
    def __init__(self, page_url, login, password, db_server, db_name, db_login, db_password):
        self.page_url = page_url
        self.login = login
        self.password = password
        self.db_server = db_server
        self.db_name = db_name
        self.db_login = db_login
        self.db_password = db_password


class TestData:
    def __init__(self, contractor_name, gross_amount, vat_amount, vat_in_pln_amount):
        self.contractor_name = contractor_name
        self.gross_amount = gross_amount
        self.vat_amount = vat_amount
        self.vat_in_pln_amount = vat_in_pln_amount


class TestDocuments:
    def __init__(self, invoice, contractor, cost_invoice, repayment, payment, loan):
        self.invoice = invoice
        self.contractor = contractor
        self.cost_invoice = cost_invoice
        self.repayment = repayment
        self.payment = payment
        self.loan = loan


#get_environment = os.environ['environment']
get_environment = 'RC'


# środowisko RC
environment_rc = TestSettings('XXXXX', 'XXXXX', 'XXXXX',
                              'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX')

invoice_vat_rc = TestData('F.H.U. FOLPAK', '2000,01', '100,02', '400,00')
invoice_no_vat_rc = TestData('F.H.U. FOLPAK', '1000,01', '0,00', '0,00')
invoice_is_sp_rc = TestData('F.H.U. FOLPAK', '1000,01', '100,02', '400,00')
invoice_is_sp_eur_rc = TestData('F.H.U. FOLPAK', '1000,01', '100,02', '400,00')

documents_rc = TestDocuments('FV20220517151846', 'F.H.U. FOLPAK', 'N-2021/10/124', '3993', '1HYJQ005IA', '2021/09/48766')


# środowisko QA
# environment_qa = TestSettings('XXX', 'XXX', 'XXX')
# invoice_vat_qa = TestData('F.H.U. FOLPAK', '1000,01', '100,02', '400,00')


def set_environment_variables(get_environment=get_environment):
    if get_environment == 'RC':
        environment = environment_rc
        invoice_vat = invoice_vat_rc
        invoice_no_vat = invoice_no_vat_rc
        invoice_is_sp = invoice_is_sp_rc
        invoice_is_sp_eur = invoice_is_sp_eur_rc
        documents = documents_rc
        return environment, invoice_vat, invoice_no_vat, invoice_is_sp, invoice_is_sp_eur, documents
    elif get_environment == 'QA':
        # environment = environment_qa
        # invoice_vat = invoice_vat_qa
        # invoice_no_vat = invoice_no_vat_qa
        # invoice_is_sp = invoice_is_sp_qa
        # invoice_is_sp_eur = invoice_is_sp_eur_qa
        pass
    else:
        print('Nieznane środowisko. Testy możliwe tylko na RC i QA. Dodaj nowe dane na nowe środowisko.')


environment, invoice_vat, invoice_no_vat, invoice_is_sp, invoice_is_sp_eur, documents = set_environment_variables()


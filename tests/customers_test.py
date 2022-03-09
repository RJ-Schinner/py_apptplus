from py_apptplus.customers import *
import os


creds = {
    'user': os.environ.get('APPT_PLUS_USER'),
    'pass': os.environ.get('APPT_PLUS_PASS'),
    'baseURL': 'https://ws.appointment-plus.com'
}

CUSTV1 = CustomersV1(creds)
customer = CUSTV1.getCustomer(330379)

print(customer.email)
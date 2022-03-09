from py_apptplus.appointments import *
import os


creds = {
    'user': os.environ.get('APPT_PLUS_USER'),
    'pass': os.environ.get('APPT_PLUS_PASS'),
    'baseURL': 'https://ws.appointment-plus.com'
}

APPTSV1 = AppointmentsV1(creds)

appointments = APPTSV1.getAppointmentsInRange(datetime.strptime('20220301', '%Y%m%d'), datetime.strptime('20220303', '%Y%m%d'))

for appt in appointments:
    print(appt.date)
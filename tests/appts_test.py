from py_apptplus.appointments import *
import os


creds = {
    'user': os.environ.get('APPT_PLUS_USER'),
    'pass': os.environ.get('APPT_PLUS_PASS'),
    'baseURL': 'https://ws.appointment-plus.com'
}

APPTSV1 = AppointmentsV1(creds)

appointments = APPTSV1.getAppointments('P1338850')
print(appointments[0].startTime)


for appt in appointments:
    print(appt.date)
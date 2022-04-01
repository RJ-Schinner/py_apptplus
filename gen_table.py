from py_apptplus.locations import *
from py_apptplus.appointments import *
import os
import pandas as pd
from  datetime import datetime, timedelta

creds = {
    'user': os.environ.get('APPT_PLUS_USER'),
    'pass': os.environ.get('APPT_PLUS_PASS'),
    'baseURL': 'https://ws.appointment-plus.com'
}

APTSV1 = AppointmentsV1(creds)
now = datetime.now()
start = now - timedelta(days=30)
end = now + timedelta(days=150)
appts = APTSV1.getAppointmentsInRange(start, end)

data = [{
    'location_id': apt.locationID,
    'customer_id': apt.customerID,
    'start_time': apt.startTime,
    'end_time': apt.endTime,
    'po_number': apt.poNumber,
    'status_desc': apt.statusDesc

} for apt in appts]

df = pd.DataFrame(data)

print(df)


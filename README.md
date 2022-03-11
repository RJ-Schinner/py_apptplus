# py_apptplus
An easy to use API Wrapper for the [Appointment Plus API](https://daysmartappointments.stoplight.io/docs/appointment-plus-api) written in Python. 

## Overview
 Appointment PLus is online appointment scheduling software. They also maintain and provide access to their RESTFUL API endpoints. py_apptplus is a high-level python library that allows the easy calling to the various endpoints available in appointment plus api. See below for a list of categories and endpoints that are currently supported in the library.


## Supported API Categories & Endpoints

### Appointments
* [GetAppointments](https://daysmartappointments.stoplight.io/docs/appointment-plus-api/b3A6MzA3OTI1ODE-get-appointments): Returns the details for appointments.
* [GetOpenDates](https://daysmartappointments.stoplight.io/docs/appointment-plus-api/b3A6MzA3OTI1ODY-get-open-dates): The method will return all available dates between start_date + num_days. If start_date is not specified, it will default to today’s date.
* [GetOpenSlots](https://daysmartappointments.stoplight.io/docs/appointment-plus-api/b3A6MzA3OTI1ODU-get-open-slots): Returns all available time slots for `num_days` number of days after the `start_date` date.

### Customers
* [GetCustomers](https://daysmartappointments.stoplight.io/docs/appointment-plus-api/b3A6MzA3OTI1OTQ-get-customers): Returns the details for customers.


### Locations
* [GetLocations](https://daysmartappointments.stoplight.io/docs/appointment-plus-api/b3A6MzA3OTI2MDI-get-locations): Returns the details for all locations.

## Examples
### Getting Appointments within a range
```
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
```
### Getting Location Info with location_id
```
from py_apptplus.locations import *
import os

creds = {
    'user': os.environ.get('APPT_PLUS_USER'),
    'pass': os.environ.get('APPT_PLUS_PASS'),
    'baseURL': 'https://ws.appointment-plus.com'
}

LOCSV1 = LocationsV1(creds)
allLocs = LOCSV1.getAllLocations()

for loc in allLocs:
    print(loc.locationName)
```

### Getting Customer Info with customer_id
```
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
```

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
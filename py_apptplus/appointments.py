from urllib.parse import urlencode
from py_apptplus.appt_plus_request import ApptPlusRequest
from datetime import datetime
import os, urllib3, json

class Appointment:
    def __init__(self, rawAppt:dict) -> None:
        self._locationID:str = rawAppt['c_id'] 
        self._apptID:str = rawAppt['appt_id']
        self._customerID:str = rawAppt['customer_id']
        self._employeeID:str = rawAppt['employee_id']
        self._dealerName:str = rawAppt['dealer_name']
        self._poNumber:str = rawAppt['po_number']
        self._lastName:str = rawAppt['last_name']
        self._firstName:str = rawAppt['first_name']
        self._email:str = rawAppt['email']
        self._staffScreenName:str = rawAppt['staff_screen_name']

        #Date info
        self._date:str = rawAppt['date']
        self._startTime:int = rawAppt['start_time']
        self._endTime:int = rawAppt['end_time']
        self._createdOn:str = rawAppt['createTimestamp']
        self._lastUpdated:str = rawAppt['lastUpdateTimestamp']

        #Cost and Status info
        self._service:str = rawAppt['service']
        self._statusDesc:str = rawAppt['appt_status_description']

    @property
    def locationID(self) -> str:
        return self._locationID

    @property
    def apptID(self) -> str:
        return self._apptID

    @property
    def customerID(self) -> str:
        return self._customerID

    @property
    def employeeID(self) -> str:
        return self._employeeID

    @property
    def dealerName(self) -> str:
        return self._dealerName

    @property
    def poNumber(self) -> str:
        return self._poNumber

    @property
    def lastName(self) -> str:
        return self._lastName

    @property
    def firtName(self) -> str:
        return self._firstName

    @property
    def email(self) -> str:
        return self._email

    @property 
    def staffScreenName(self) -> str:
        return self._staffScreenName

    @property
    def date(self) -> str:
        return self._date

    @property
    def startTime(self) -> str:
        return self._startTime

    @property
    def endTime(self) -> str:
        return self._endTime

    @property
    def createdOn(self) -> str:
        return self._createdOn

    @property
    def lastUpdated(self) -> str:
        return self._lastUpdated

    @property
    def service(self) -> str:
        return self._service

    @property
    def statusDesc(self) -> str:
        return self._statusDesc


class AppointmentsV1(ApptPlusRequest):

    #This method allows us to get all of the appointments between start and end
    def getAppointmentsInRange(self, start:datetime, end:datetime) -> list[Appointment]:
        #Build URL with query params (cant use fields parameter cause its a POST request)
        qParams = {
            'response_type':'json',
            'start_date':start.strftime('%Y%m%d'),
            'end_date':end.strftime('%Y%m%d')}

        apiURL = f'{self.baseURL}/Appointments/GetAppointments?{urlencode(qParams)}'

        rawResp:dict = json.loads(self.doPOST(apiURL).data.decode('utf-8'))

        return [Appointment(rawAppt) for rawAppt in rawResp['data']]

    
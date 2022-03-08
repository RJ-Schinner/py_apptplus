from py_apptplus.appt_plus_request import ApptPlusRequest
import os, urllib3


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
    def getAppointmentsInRange(self, start, end) -> list[Appointment]:
        pass
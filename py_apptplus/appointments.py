from urllib.parse import urlencode
from py_apptplus.appt_plus_request import ApptPlusRequest
from datetime import datetime
import json

class Appointment:
    def __init__(self, rawAppt:dict) -> None:
        self._locationID:str = rawAppt['c_id'] 
        self._apptID:str = rawAppt['appt_id']
        self._customerID:str = rawAppt['customer_id']
        self._employeeID:str = rawAppt['employee_id']
        self._dealerName:str = rawAppt['dealer_name'] if rawAppt.get('dealer_name') else None
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

class OpenDate:
    def __init__(self, rawOpenDate:dict) -> None:
        self._cID:str = rawOpenDate['c_id'] #location_id
        self._date:str = rawOpenDate['date']

    @property
    def cID(self) -> str:
        return self._cID

    @property
    def date(self) -> datetime:
        return datetime.strptime(self._date, '%Y%m%d')

class OpenSlot:
    def __init__(self, rawOpenSlot:dict) -> None:
        self._cID:str = rawOpenSlot['c_id']
        self._date:str = rawOpenSlot['date']
        self._startTime:str = rawOpenSlot['start_time']
        self._gmtTimestamp:str = rawOpenSlot['gmt_timestamp']

    @property
    def cID(self) -> str:
        return self._cID

    @property
    def date(self) -> str:
        return self._date

    @property
    def startTime(self) -> str:
        return self._startTime

    @property
    def gmtTimestamp(self) -> str:
        return self._gmtTimestamp

#The AppointmentsV1 class is the class that wraps the calling to
#the various Appointments api endpoints into easy to use methods.
#That is this class and its methods are the ones actually using an
#http client to make requests to the api.
class AppointmentsV1(ApptPlusRequest):

    #This method allows us to get all of the appointments between start and end
    def getAppointmentsInRange(self, start:datetime, end:datetime) -> list[Appointment]:
        #Build URL with query params (cant use fields parameter cause its a POST request)
        qParams = {
            'response_type':'json',
            'start_date':start.strftime('%Y%m%d'),
            'end_date':end.strftime('%Y%m%d')}

        #Make Request
        apiURL = f'{self.baseURL}/Appointments/GetAppointments?{urlencode(qParams)}'
        rawResp:dict = json.loads(self.doPOST(apiURL).data.decode('utf-8'))
        
        if rawResp['data']:
            return [Appointment(rawAppt) for rawAppt in rawResp['data']]

    #Returns the dates that are available for scheduling. The method will
    #return all available dates between start_date + num_days. if start_date
    #is not specified, it will default to today's date.
    def getOpenDates(self, numDays:int, startDate:datetime = None) -> list[OpenDate]:
        #Build URL
        qParams:dict = {
            'response_type':'json',
            'num_days':numDays
        }

        if startDate:
            qParams['start_date'] = startDate.strftime('%Y%m%d')

        #Make Request
        apiURL:str = f'{self.baseURL}/Appointments/GetOpenDates?{urlencode(qParams)}'
        rawResp:dict = json.loads(self.doPOST(apiURL).data.decode('utf-8'))

        if rawResp['data']:
            return [OpenDate(rawOpenDate) for rawOpenDate in rawResp['data']]

    def getOpenSlots(self, startDate:datetime, numDays:int, locationID:int = None) -> list[OpenSlot]:
        #Build URL 
        qParams:dict = {
            'start_date' : startDate.strftime('%Y%m%d'),
            'num_days' : numDays
        }

        if locationID:
            qParams['location_id'] = locationID

        apiURL:str = f'{self.baseURL}/Appointments/GetOpenSlots?{urlencode(qParams)}'
        rawResp:dict = json.loads(self.doPOST(apiURL).data.decode('utf-8'))

        if rawResp['data']:
            return [OpenSlot(rawOpenSlot) for rawOpenSlot in rawResp['data']]
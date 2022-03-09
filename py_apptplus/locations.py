
from urllib.parse import urlencode
from py_apptplus.appt_plus_request import ApptPlusRequest
from datetime import datetime
import json

class Location:
    def __init__(self, rawLocation:dict) -> None:
        self._locationID:int = int(rawLocation['location_id'])
        self._isHeadquarters:bool = True if rawLocation['headquarters'] == 'Y' else False
        self._name:str = rawLocation['name']
        self._locationName:str = rawLocation['location_name']
        self._headquartersID:int = int(rawLocation['headquarters_id'])
        self._clientType:int = int(rawLocation['client_type'])
        self._status:int = int(rawLocation['status'])
        self._address1:str = rawLocation['address1']
        self._address2:str = rawLocation['address2']
        self._city:str = rawLocation['city']
        self._state:str = rawLocation['state']
        self._zip:str = rawLocation['zip']
        
        #Contact info
        self._phone:str = rawLocation['phone']
        self._email:str = rawLocation['email']
        
        #Appointplus GUI info
        self._customerInterfaceURL:str = rawLocation['customerInterfaceUrl']
        self._bookID:str = rawLocation['book_id']

    @property
    def locationID(self) -> int:
        return self._locationID

    @property
    def isHeadquarters(self) -> bool:
        return self._isHeadquarters

    @property
    def name(self) -> str:
        return self._name

    @property
    def locationName(self) -> str:
        return self._locationName
    
    @property
    def headquartersID(self) -> int:
        return self._headquartersID

    @property
    def clientType(self) -> int:
        return self._clientType

    @property
    def status(self) -> int:
        return self._status

    @property
    def address(self) -> str:
        if not self._address2:
            return self._address1

        return f'{self._address1} {self._address2}'

    @property
    def city(self) -> str:
        return self._city

    @property
    def state(self) -> str:
        return self._state

    @property
    def zip(self) -> str:
        return self._zip

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def email(self) -> str:
        return self._email

    @property
    def customerInterfaceUrl(self) -> str:
        return self._customerInterfaceURL

    @property
    def bookID(self) -> str:
        return self._bookID

class LocationsV1(ApptPlusRequest):

    #This method retrieves information about one specific location
    #with id "locationID"
    def getLocation(self, locationID:int) -> Location:
        #Build URL
        qParams:dict = {
            'response_type': 'json',
            'c_id': locationID
        }
        apiURL:str = f'{self.baseURL}/Locations/GetLocations?{urlencode(qParams)}'

        #Make request
        resp:dict = self.doPOST(apiURL)

        #Make sure data is there and return a Location object
        #if there is
        if resp['data']:
            return Location(resp['data'][0])
    
    #This method retrieves a list of all the locations set up in the
    #appointments plus system, and all the relevant information about
    #a location
    def getAllLocations(self) -> list[Location]:
        #Build URL
        qParams:dict = {
            'response_type': 'json',
            'status': 1 #A status of 1 implies the location is active
        }
        apiURL:str = f'{self.baseURL}/Locations/GetLocations?{urlencode(qParams)}'

        #Make request
        resp:dict = self.doPOST(apiURL)

        #Make sure data is there and return a Location object
        #if there is
        if resp['data']:
            return [Location(rawLoc) for rawLoc in resp['data']]
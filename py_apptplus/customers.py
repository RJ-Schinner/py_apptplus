from urllib.parse import urlencode
from py_apptplus.appt_plus_request import ApptPlusRequest

class Customer:
    def __init__(self, rawCust:dict) -> None:
        self._customerID:int = int(rawCust['customer_id'])
        self._firstName:str = rawCust['first_name']
        self._lastName:str = rawCust['last_name']
        self._cellPhone:str = rawCust['cell_phone']
        self._email:str = rawCust['email']
        self._employeer:str = rawCust['employer']

    @property
    def customerID(self) -> int:
        return self._customerID

    @property
    def firstName(self) -> str:
        return self._firstName

    @property
    def lastName(self) -> str:
        return self._lastName

    @property
    def cellPhone(self) -> str:
        return self._cellPhone

    @property
    def email(self) -> str:
        return self._email

    @property
    def employer(self) -> str:
        return self._employeer

#The CustomersV1 class wraps the calling to the Customers API endpoint.
#The methods in this class return either a list of "Location" objects or
#a single "Location" object.
class CustomersV1(ApptPlusRequest):
    #Retrieves a single customer with ID "customerID" from the 
    #appointment plus Customers API.
    def getCustomer(self, customerID:int) -> Customer:
        #Build URL
        qParams:dict = {
            'response_type': 'json',
            'customer_id': customerID
        }
        apiURL:str = f'{self.baseURL}/Customers/GetCustomers?{urlencode(qParams)}'

        #Make Request
        resp:dict = self.doPOST(apiURL)

        #Make sure there is actually something to return and if
        #there is we return it
        if resp['data']:
            return Customer(resp['data'][0])

    #Updates field(s) for a particular customer in the appointment plus system. 
    #The customer to be updated is passed as a parameter to the method.
    def updateCustomer(self): 
        pass

    #This method deletes a single customer from the appointment plus system
    #the customer to be deleted is the customer passed to the method as a 
    #parameter "customerID". !!DELETING A CUSTOMER ALSO DELETES THEIR APPTS,
    #NOTES, PETS/CHILDREN, WAITING LIST ENTRIES, ASSIGNED PACKAGES AND FUTURE 
    #SMS REMINDERS!! Once deleted the customer record cannot be restord.
    def deleteCustomer(self, customerID:str) -> bool:
        #Build URL
        qParams:dict = {
            'response_type':'json',
            'customer_id':customerID}
        apiURL:str = f'{self.baseURL}/Customers/DeleteCustomers?{urlencode(qParams)}'

        #Make request
        resp:dict = self.doPOST(apiURL)

        if resp['result'] == 'success':
            return True

        return False
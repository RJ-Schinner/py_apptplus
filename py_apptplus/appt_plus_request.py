from base64 import b64encode
from http.client import responses
from urllib.parse import urlencode
from urllib3 import PoolManager, HTTPResponse
from py_apptplus.appt_plus_exceptions import ApptPlusException

class ApptPlusRequest:

    def __init__(self, credentials:dict) -> None:
        self._baseURL:str = credentials['baseURL']
        #The appointment plus api uses your username:password as a 
        #base64 encoded string as its means for authorization
        self._basicAuth = b64encode(f'{credentials["user"]}:{credentials["pass"]}'.encode('ascii')).decode()
        
        #Setting up http client
        self._headers:dict = {'Authorization': f'Basic {self._basicAuth}'}
        self._httpClient:PoolManager = PoolManager(headers=self._headers)

    @property
    def baseURL(self) -> str:
        return self._baseURL

    @property
    def httpClient(self) -> PoolManager:
        return self._httpClient

    def doPOST(self, apiURL:str) -> HTTPResponse:
        self._headers['Content-Type'] = 'application/json'
        rawResp:HTTPResponse = self.httpClient.request('POST', apiURL, headers=self._headers)
        del self._headers['Content-Type']

        if rawResp.status == 200:
            return rawResp

        else:
            raise ApptPlusException(
                self.__class__.__name__,
                'Request to Branches endpoint failed',
                f'doPOST({apiURL}): {rawResp.status} - {responses[rawResp.status]}'
            )
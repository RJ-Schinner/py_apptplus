from base64 import b64encode
from http.client import responses
from urllib3 import PoolManager, HTTPResponse
from py_apptplus.appt_plus_exceptions import ApptPlusException
import json

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

    def doPOST(self, apiURL:str, noContentType:bool=False) -> HTTPResponse:
        if not noContentType:
            self._headers['Content-Type'] = 'application/json'
        
        rawResp:HTTPResponse = self.httpClient.request('POST', apiURL, headers=self._headers)
        #Make sure the request returned a 200 code, and additonalys check
        #the "result" field in the response and check that it says "success"
        resp:dict = json.loads(rawResp.data.decode('utf-8'))
        if rawResp.status == 200 and resp.get('result') == 'success':
            return resp

        else:
            raise ApptPlusException(
                self.__class__.__name__,
                'Request to Branches endpoint failed',
                f'doPOST({apiURL}): {rawResp.status} - {responses[rawResp.status]}'
            )
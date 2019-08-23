import sys
import requests
from st2common.runners.base_action import Action

class KennyAction (Action):
    def run(self, url):
        try:
                response = requests.get( url )
                print ( response.status_code )
                print (response.url)
        except  requests.exceptions.MissingSchema:
                print ( 'UnSuccessful!' )
                sys.exit(0)


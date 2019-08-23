import requests
from st2common.runners.base_action import Action

class KennyAction (Action) :
    def run(self, url) :
        response = requests.get ( url )
        print ( response.status_code )

    print ( response.url )


    if (response==200)
        print ( 'Successful!' )
    else :
        print ( 'An error occurred.' )


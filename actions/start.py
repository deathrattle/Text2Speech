import requests
class KennyAction(Action):
def run(self, url):
response = requests.get(url)
		print(response.status_code)
print(response.url)
if response:
    print('Success!')
else:
    print('An error has occurred.')

import requests
class KennyAction(Action):
def run(self, url):
response= requests.get(url)
		print(response.status_code)
print(response.url)
if response:
    print('Successful!')
else:
    print('An error occurred.')

import json
import urllib.request as request

with request.urlopen('https://quotes.rest/qod') as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source.decode('utf-8'))
    else:
        print('An error occurred while attempting to retrieve data from the API.')

print(data['contents'])
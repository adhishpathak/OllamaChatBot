import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth
import base64

load_dotenv()

# Your API key and secret
api_key = os.getenv('api_key')
secret_key = os.getenv('secret_key')



# Define the start and end times in the format YYYYMMDDTHH
start_time = '20240930T00'
end_time = '20241001T23'

# Amplitude Export API endpoint
url = f'https://amplitude.com/api/2/export?start={start_time}&end={end_time}'

# Base64 encoding of the API key and secret key for basic authentication
auth = HTTPBasicAuth(api_key, secret_key)

# Send the GET request
response = requests.get(url, auth=auth)

# Handle the response
if response.status_code == 200:
    # The response is a zipped archive of JSON files
    with open('exported_data.zip', 'wb') as f:
        f.write(response.content)
    print('Data exported successfully.')
elif response.status_code == 404:
    print('No data available for the requested time range.')
else:
    print(f'Failed to export data. Status code: {response.status_code}')

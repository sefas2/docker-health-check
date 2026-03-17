import requests
import os
import datetime


URL = os.environ.get('TARGET_HOST')
response = requests.get(URL)
time_date = datetime.datetime.now()
status = f"{time_date} - Health check successful:{response.status_code}"
print(status)

with open('/app/report.txt', 'w') as f:
    f.write(status)

import requests
import os

URL = os.environ.get('TARGET_HOST')
response = requests.get(URL)
status = f"Health check successful:{response.status_code}"

with open('/app/report.txt', 'w') as f:
    f.write(status)

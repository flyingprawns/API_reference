import requests  # The most popular library for API interfacing. Not a default module, must manually install.

API_URL = "http://api.open-notify.org/iss-now.json"  # API Endpoint - my program sends its request here

response = requests.get(url=API_URL)  # Returns an HTTP response code
response.raise_for_status()  # Raises an exception for unsuccessful response codes

# Retrieve ISS coordinates from data
data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)
print(iss_position)

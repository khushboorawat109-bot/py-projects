import requests
val = input("Enter City: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={val}&appid=9b1c8e5a0c3d2f1e7a4b8c9d0e6f7g8"
response = requests.get(url)
data = response.text
print(weather)
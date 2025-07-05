import requests

url = "http://127.0.0.1:8000/send-email"
data = {
    "host": "smtp.gmail.com",
    "to": "sohan100karfa@gmail.com",
    "subject": "hello",
    "body": "hi"
}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())

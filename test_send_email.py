import requests

url = "https://your-service-name- RANDOM_HASH-uc.a.run.app/send-email" #<-- IMPORTANT: Replace with your Cloud Run URL
data = {
    "host": "smtp.gmail.com",
    "to": "<mail>@gmail.com",
    "subject": "<subject>",
    "body": "<body>"
}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())

import requests

url = "http://localhost:9696/predict"

client = {"job": "retired", "duration": 445, "poutcome": "success"}

try:
    response = requests.post(url, json=client)
    response.raise_for_status()  # Raise an error for non-2xx status codes
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except ValueError as e:
    print(f"Response parsing error: {e}")
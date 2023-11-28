import requests
import os
from dotenv import load_dotenv

load_dotenv()

s = os.environ.get("MY_ENV")

if s is not None:
    print(s)
else:
    r = requests.get('http://127.0.0.1:5000/about')
    print(f"Результат виконання запиту за допомогою бібліотеки requests: {r.text}")
import requests

r = requests.get('http://127.0.0.1:5000/about')

print(f"Результат виконання запиту за допомогою бібліотеки requests: {r.text}")
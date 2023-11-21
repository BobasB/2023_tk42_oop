import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

print(f"Результат виконання запиту за допомогою бібліотеки requests: {r.status_code}")
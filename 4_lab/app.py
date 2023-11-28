from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f'Привіт, ми виводимо змінну середовища: {os.environ.get("MY_ENV")}'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

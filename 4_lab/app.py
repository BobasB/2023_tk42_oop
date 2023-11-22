from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Привіт, це мій перший веб-сайт на Flask!'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

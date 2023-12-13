from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# Define routes
@app.route('/')
def home():
    return render_template('index.html', title='Home', content='Welcome to Dark Duck Comics!')


@app.route('/about')
def about():
    return render_template('about.html', title='About', content="We are a small start-up company of Husband and Wife"
                                                                " who love comics and conventions.")


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', content='Contact us on <a href='
                                                                    '"https://www.instagram.com/darkduckcomics/"'
                                                                    ' target="_blank">Instagram</a>.')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

"""
Python program that creates a local web page
pages render from a folder named templates that hold the html code
"""
from datetime import datetime
import re
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'super secret key'

users = {}


def validate_password(password):
    if len(password) < 12:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in to access this page', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists', 'danger')
        elif not validate_password(password):
            flash('Password does not meet complexity requirements', 'danger')
        else:
            users[username] = password
            flash('Registration successful, please login', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users or users[username] != password:
            flash('Invalid username or password', 'danger')
        else:
            session['username'] = username
            flash('Login successful', 'success')
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


@app.route('/')
def home():
    """
    home page
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)


@app.route('/about')
def about():
    """
    about page
    """
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('about.html')


@app.route('/contact')
def contact():
    """
    contact page
    """
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

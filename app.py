from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key in production

# Dummy database (replace this with your MySQL database connection)
users = []

# Route for the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route for processing login form data
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    # Check login credentials (replace this with your database check)
    for user in users:
        if user['email'] == email and user['password'] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))

    flash('Invalid email or password. Please try again.', 'error')
    return redirect(url_for('login'))

# Route for the registration page
@app.route('/register')
def register():
    return render_template('register.html')

# Route for processing registration form data
@app.route('/register', methods=['POST'])
def register_post():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    phone = request.form.get('phone')

    # Check if the email is already registered (replace this with your database check)
    for user in users:
        if user['email'] == email:
            flash('Email is already registered. Please use a different email.', 'error')
            return redirect(url_for('register'))

    # Add the new user to the database (replace this with your database insertion)
    users.append({'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password, 'phone': phone})

    flash('Registration successful! You can now log in.', 'success')
    return redirect(url_for('login'))

# Route for the dashboard (replace this with your actual dashboard route)
@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
    app.run(debug=True)

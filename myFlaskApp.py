from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return "Hello, World!"

# Define another route (optional)
@app.route('/about')
def about():
    return "This is the About page!"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template


from flask_cors import CORS

app = Flask(__name__, template_folder='templates')

CORS(app)


# Render Main Page
@app.route('/')
def index():
    return render_template('index.html')


# About Page
@app.route('/about')
def about():
    return render_template('about.html')


# Appointment Page
@app.route('/appointment')
def appointment():
    return render_template('appointment.html')


# Render Resources Page
@app.route('/resources')
def resources():
    return render_template('resources.html')


# Render Contact People Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

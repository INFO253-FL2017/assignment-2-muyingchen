"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request
import os
import requests

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def home():
	"""
	If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
	returns will be sent to the browser
	"""
	return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/index')
def index():
	"""
	If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
	returns will be sent to the browser
	"""
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about_us.html")

@app.route('/contact', methods=['GET'])
def contact():
	return render_template("contact_us.html", notifications=[])

@app.route('/contact', methods=['POST'])
def contact_1():
	username = request.form.get("name")
	subject = request.form.get("subject")
	message = request.form.get("message")
	notifications = []
	data = {
		'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
		'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
		'subject': subject,
		'text': message,
	}

	auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

	r = requests.post(
		'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
		auth=auth,
		data=data)

	if r.status_code == requests.codes.ok:
		response = "Thank you " + username + ", your message has been sent."
		notifications.append(response)
	else:
		response = "Sorry " + username + ", your message was not sent. Please try again."
		notifications.append(response)
	return render_template("contact_us.html", notifications=notifications)


@app.route('/blog/8-experiments-in-motivation')
def blog1():
	return render_template("blog/8_Experiments_in_Motivation.html")

@app.route('/blog/a-mindful-shift-of-focus')
def blog2():
	return render_template("blog/A_Mindful_Shift_of_Focus.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog3():
	return render_template("blog/How_to_Develop_an_Awesome_Sense_of_Direction.html")

@app.route('/blog/training-to-be-a-good-writer')
def blog4():
	return render_template("blog/Training_to_Be_a_Good_Writer.html")

@app.route('/blog/what-productivity-systems-wont-solve')
def blog5():
	return render_template("blog/What_Productivity_Systems_Won't_Solve.html")

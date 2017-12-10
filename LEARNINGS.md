What is the function of the following technologies in your assignment:
HTML: It is templates that are being rendered by web server, it describes the representation of structures of the information in the blog.
CSS: It adds style to webpages/templates in the blog
JavaScript: It adds form validation to the contact us page.
Python: It is the language that is being used to write backend of the assignment.
Flask: The framework that we use to power the frontend and backend of the application.
HTTP: It is the protocol that connects the client (web browser) to the server (our app) so that we can view our app on a web browser.
GET and POST requests: They are HTTP requests methods that allow us (the client) to retrieve information as well as storing information from/to our web server.

How does HTML, CSS, and JavaScript work together in the browser for this assignment?
CSS adds style the HTML template content, and JavaScript adds interactivity to our static content so that our webpage content could change based on the activities being made by user.

How does Python and Flask work together in the server for this assignment?
Flask is the web framework library for Python. Together, they allow us to interact with webpages so that user could retrieve as well as store information to the web server using HTTP requests such as GET and POST.


List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
GET requests:
/  -- when the user enter "http://127.0.0.1:5000/" on the browser, index.html page is being rendered by the server to display on the browser
/index -- same as above when "http://127.0.0.1:5000/index" is entered by the browser
/contact -- when the user enter "http://127.0.0.1:5000/contact" on the browser, contact_us.html page is being rendered by the server to display on the browser
/about -- when the user enter "http://127.0.0.1:5000/about" on the browser, about_us.html page is being rendered by the server to display on the browser
/blog/8-experiments-in-motivation -- when the user enter "http://127.0.0.1:5000/blog/8-experiments-in-motivation" on the browser, 8-experiments-in-motivation.html page is being rendered by the server to display on the browser
/blog/a-mindful-shift-of-focus -- when the user enter "http://127.0.0.1:5000/blog/a-mindful-shift-of-focus" on the browser, a-mindful-shift-of-focus.html page is being rendered by the server to display on the browser
/blog/how-to-develop-an-awesome-sense-of-direction -- when the user enter "http://127.0.0.1:5000/blog/how-to-develop-an-awesome-sense-of-direction" on the browser, how-to-develop-an-awesome-sense-of-direction.html page is being rendered by the server to display on the browser
/blog/training-to-be-a-good-writer -- when the user enter "http://127.0.0.1:5000/blog/training-to-be-a-good-writer" on the browser, training-to-be-a-good-writer.html page is being rendered by the server to display on the browser
/blog/what-productivity-systems-wont-solve -- when the user enter "http://127.0.0.1:5000/blog/what-productivity-systems-wont-solve" on the browser, what-productivity-systems-wont-solve.html page is being rendered by the server to display on the browser

POST request:
/contact -- when user entered information and click "submit" button on the contact form, the browser will send a POST request to the web server for processing the data, in this case is to send an email to the website owner

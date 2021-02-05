"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from flask import Flask, render_template

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''

# The first route/page
@app.route('/')
def home():
    return 'My home page'

# The about route/page
@app.route('/about')
def about():
    return render_template('about.html')

# The default route/page - unknown urls lead here
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    # app.run()
    # Tells FLask how to start the development server
    app.run(debug=True, host="0.0.0.0", port=8080)

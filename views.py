"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
import smtplib


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/send', method = ['POST'])
def sendemail():
    username = 'duanelewis88@gmail.com'
    password = 'nfkdxlhdicvehlez'
    
    fromname = request.form['name']
    fromemail = request.form['email']
    fromsubject = request.form['subject']
    msg = request.form['msg']
    toemail = username
    message = """From: {} <{}>
    To: {} <{}>
    Subject: {}
    {}
    """

    messagetosend = message.format(
                              fromname,
                              fromemail,
                              "Email Form",
                              toemail,
                              fromsubject,
                              msg)
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromemail,toemail,fromsubject,messagetosend)
    server.quit()
    return render_template('email.html', time=time_info())
  
def time_info():
  now = time.strftime("%a %d %b %Y")
  return now
      
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")

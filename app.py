from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def greet_welcome():
    '''Returns the welcome landing page'''
    return '''<html><body><h1>welcome</h1></body></html>'''
   

@app.route('/welcome/home')
def greet_welcome_home():
    '''Returns the welcome home page'''
    return '''<html><body><h1>welcome home</h1></body></html>'''
   

@app.route('/welcome/back')
def greet_welcome_back():
    '''Returns the welcome back page'''
    return '''<html><body><h1>welcome back</h1></body></html>'''
  
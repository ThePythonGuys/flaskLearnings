import ipaddress
import string, random
import requests
import getpass

from flask import Flask, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators,\
SelectField
import flask

app = Flask(__name__)

#Forms from WTForms
class AkaForm(Form):
    aka = StringField("Client Facing URL:")

#Functions to do stuff with python
def id_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def aka_gen(url):
    ourl = "aka-" + id_generator() + "-" + url
    return ourl

#URI definitions per script
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/aka", methods=['GET', 'POST'])
def create_aka_obs():
    form = AkaForm(request.form)
    if request.method == "GET":
        return render_template('aka-obf.html', form=form)
    if request.method == "POST":
        akagen = aka_gen(form.aka.data)
        return render_template('aka-obf-post.html', akagen=akagen)
    return render_template('about.html')

if __name__ == '__main__':
    app.run()

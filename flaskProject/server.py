import os
from db_init import initialize

from flask import Flask, redirect, url_for, render_template, request, Blueprint

from psycopg2 import extensions
from queries import *

from views.actor import actor
from views.movie import movie
#türkçe karakter için

extensions.register_type(extensions.UNICODE)
extensions.register_type(extensions.UNICODEARRAY)
"""
Blueprint benzer sayfalardan çok omasını önlemek ve server.py dosyasında 
çok sayfalı projelerde yer kaplamamak için kullanılır.

"""



app = Flask(__name__, template_folder='templates')

#Blueprintleri import etmemiz lazım appin üstüne
app.register_blueprint(actor,url_prefix="/actors")
app.register_blueprint(movie,url_prefix="/movies")


#movies = ["Movie1" , "Movie2" , "Movie3" , "Movie4"]


#Herokuyu kullanacağımız zaman True yapıyoruz.
HEROKU = True

if(not HEROKU):
    os.environ['DATABASE_URL'] = "dbname= 'postgres' user='postgres' host='localhost' password='399130'"
    initialize(os.environ['DATABASE_URL'])
@app.route("/")
def anaSayfa():
    return render_template("index.html")



"""
@app.route("/welcome<name>")
def welcome_page(name):
    return "<p> Welcome {} {} </p>".format(name,123)

"""


if __name__ == '__main__':
    if(not HEROKU):
        app.run(debug=True)
    else:
        app.run()

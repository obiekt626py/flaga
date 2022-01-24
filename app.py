from flask import Flask, render_template
import os
import requests


app=Flask(__name__)

@app.route('/')
def index():
    
    
    text = open('xd.txt').read()
    
    return render_template("index.html", text=text)

@app.route('/xd')
def index():
    
    strona_flag = requests.get('https://zajecia-programowania-xd.pl/flagi')
    
    text = {'d1':'x'}
    
    return render_template("xd.html", text=text)
    
if __name__=="__main__":
    app.run()

#Terminalban:
#cd "C:\Users\Asus\Documents\Visual Studio Code\First-python-project"
#flask run vagy python app.py
#localhost: 127.0.0.1:5000/

from flask import Flask, render_template, request

app = Flask(__name__) # Flask alkalmazás létrehozása


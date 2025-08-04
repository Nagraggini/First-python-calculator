#Terminalban:
#cd "C:\Users\Asus\Documents\Visual Studio Code\First-python-project"
#flask run vagy python app.py
#localhost: 127.0.0.1:5000/

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Helló, működik a Flask!"

if __name__ == "__main__":
    app.run(debug=True)
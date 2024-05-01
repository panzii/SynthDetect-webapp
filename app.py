from flask import Flask, render_template, request, redirect, url_for
import os



app = Flask(__name__)





@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/demo", methods=['GET'])
def demo():
    return render_template('demo.html')

@app.route("/team", methods=['GET'])
def team():
    return render_template('team.html')



if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')

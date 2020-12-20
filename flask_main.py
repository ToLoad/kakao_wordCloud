from make_wordcloud import make_png
from flask import Flask, render_template, request, redirect
import pandas as pd
import sys

app = Flask("Kakao Chat Analyze")

@app.route("/")
def home():
    return render_template("mainPage.html")

@app.route('/file_uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST': # POST 방식으로 전달된 경우
        f = request.files['file']
        make_png('준혁이', f)
        return render_template("wordCloud.html")
        # return "successed"

app.run(port='8000', debug=True)






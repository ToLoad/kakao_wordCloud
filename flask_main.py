from make_wordcloud import make_png
from analyze_text import get_id
from flask import Flask, render_template, request, redirect
import pandas as pd
import sys

app = Flask("Kakao Chat Analyze")

@app.route("/")
def home():
    return render_template("mainPage.html")

@app.route('/make_wc', methods = ['GET', 'POST'])
def make_wc():
    if request.method == 'POST':
        f = request.files['file']
        id = request.form['input_id']
        mode = request.form['contact']
        return make_png(id, f, mode)

@app.route('/get_idlist', methods = ['GET', 'POST'])
def get_idlist():
    if request.method == 'POST':
        f = request.files['file']
        mode = request.form['contact']
        getIdList = get_id(f, mode)
        return render_template("wordCloud.html", getID=getIdList)

if __name__ == "__main__":
    app.run()





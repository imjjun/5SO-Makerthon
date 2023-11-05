from flask import Flask, jsonify, request, render_template, url_for
import sqlite3 as sql
import datetime
import base64
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/upload", methods = ["POST"])
def upload():
    maskfile = request.get_json()
    if maskfile['name']==None:
        maskfile['name']=="변우중"
    now = datetime.datetime.now()
    current = now + datetime.timedelta(hours=9)
    image = maskfile['image']
    image1 = image[0]
    path = 'static/img' 
    file_list = os.listdir(path) 
    bytes_base64 = image1["data"]
    data = base64.b64decode(bytes_base64)
    open("static/img/{}.jpg".format(len(file_list)),'wb').write(data)
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO mask(name, time, location) VALUES (?,?,?)", (maskfile['name'], current.strftime('%Y-%m-%d %H:%M:%S'), maskfile['location']))
    con.commit()
    con.close()
    return 'OK'

@app.route('/photoupload', methods = ["POST"])
def photo():
    path = 'static/img' 
    file_list = os.listdir(path) 
    photo = request.get_json()
    bytes_base64 = photo["data"].encode()
    data = base64.b64decode(bytes_base64)
    open("static/img/{}.png".format(len(file_list)),'wb').write(data)
    return 'OK'

@app.route("/photo/<int:index>/")
def show(index):
    picture = f"img/{index}.png"
    return render_template("showphoto.html", picture = picture)

if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)
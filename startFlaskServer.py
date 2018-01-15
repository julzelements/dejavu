import warnings
import json

warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer

with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

import os
import socket
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename
from redis import Redis, RedisError


redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['wav'])
UPLOADS_PATH = '/Users/julianscharf/Development/dejavu/uploads'
# UPLOADS_PATH = '/uploads'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    app.logger.debug('A GET request was made')
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Resis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
            "<b>Hostname:</b> {hostname}<br/>" \
            "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)


@app.route("/recognize", methods=['GET', 'POST'])
def recognize():
    if request.method == 'POST':
        app.logger.debug('A POST request was made')
        file = request.files['file']
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            app.logger.debug('file was nil')
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOADS_PATH, filename))

            djv = Dejavu(config)
            song = djv.recognize(FileRecognizer, UPLOADS_PATH + '/' + filename)
            return "%s" % song

    app.logger.debug('A GET request was made')
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

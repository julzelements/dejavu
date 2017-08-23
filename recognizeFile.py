import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

#
# from flask import Flask
# from flask_restful import Resource,  Api
# app = Flask('myapp')
# api = Api(app)
# api.add_resource(Recognize, '/recognize')

#
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['mp3'])
UPLOADS_PATH = '/Users/julianscharf/Development/dejavu/uploads'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/recognize", methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		file = request.files['file']
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(UPLOADS_PATH, filename))

			djv = Dejavu(config)
			song = djv.recognize(FileRecognizer, UPLOADS_PATH + '/' + filename)
			return "From file we recognized: %s\n" % song

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
	app.run(host='0.0.0.0', port=5000)


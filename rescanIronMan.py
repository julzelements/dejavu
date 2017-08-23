import warnings
import json
from time import gmtime, strftime

warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("googleCloud.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':
	print "start"
	print strftime("%Y-%m-%d %H:%M:%S", gmtime())

	# create a Dejavu instance
	djv = Dejavu(config)

	# Fingerprint all the mp3's in the directory we give it
	djv.fingerprint_directory("ironMan", [".mp3"])

	print "end"
	print strftime("%Y-%m-%d %H:%M:%S", gmtime())


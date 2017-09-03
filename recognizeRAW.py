import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

	djv = Dejavu(config)


	recognizer = FileRecognizer(djv)
	song = recognizer.recognize_file("RAW/ironManRaw.WAV")
	print "No shortcut, we recognized: %s\n" % song
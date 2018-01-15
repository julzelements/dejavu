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

	song = recognizer.recognize_file("RAW/IronMan_420-425secs.wav")
	print "No shortcut, we recognized: %s\n" % song

	song = recognizer.recognize_file("RAW/IronMan_420-425secs.mp3")
	print "No shortcut, we recognized: %s\n" % song
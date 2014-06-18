import os
from flask import Flask
from sh import unzip
from sh import lftp
from sh import forego

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Detected\nunzip:{}\nlftp:{}\nforego:{}'.format(
    	unzip("-v"),
    	lftp("-v"),
    	forego("version"),
    	)

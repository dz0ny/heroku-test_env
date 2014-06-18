import os
from flask import Flask
from sh import unzip
from sh import lftp
from sh import forego

app = Flask(__name__)


@app.route('/')
def index():
    return 'Detected\nunzip:{}\nlftp:{}\nforego:{}'.format(
        unzip("-v", _tty_out=False),
        lftp("-v", _tty_out=False),
        forego("version", _tty_out=False),
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask
from utils import get_avr


app = Flask(__name__)


@app.route('/avr_data')
def avr_data():
    file = "hw.csv"
    access = "rt"
    return get_avr(file, access)


app.run(debug=True, port=5000)

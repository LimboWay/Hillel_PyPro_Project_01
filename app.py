from flask import Flask
import utils


app = Flask(__name__)


@app.route('/')
def view():
    file = "requirements.txt"
    access = "r"
    return utils.text_to_html(file, access)


app.run(debug=True, port=12345)

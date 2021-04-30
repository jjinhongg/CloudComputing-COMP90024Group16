from flask import Flask
from flask import render_template
import time
import utils
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('template_assignemnt2.html')

@app.route('/l1')
def get_l1_data():
    pass

if __name__ == '__main__':
    app.run()

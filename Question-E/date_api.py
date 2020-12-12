from flask import Flask,jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    i = datetime.now()
    tz = pytz.timezone('US/Eastern')
    date = tz.localize(i)

    return jsonify({'date': date.strftime("%a %b %d %H:%M:%S %Z %Y")})

if __name__ == '__main__':
    app.run()

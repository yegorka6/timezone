import flask, json, requests
from flask import request

from flask import Flask
app = Flask(__name__)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_timezone(lat, long):
    response = requests.get("https://api.darksky.net/forecast/a505f129cd31c090ad499730fce56a3b/" + lat + "," + long)
    return response.json()['timezone']

@app.route('/', methods=['GET'])
def home():
    return "<h1>Forecast API</h1><p>This site is a prototype API for the forecast API.</p>"

@app.route('/endpoint', methods=['GET'])
def api_id():
    result = ''
    if 'lat' in request.args and 'long' in request.args:
        lat = str(request.args['lat'])
        long = str(request.args['long'])
        result = get_timezone(lat, long)
    else:
        return "Error: No latitude/longtitude provided. Please specify an latitude and longtitude."

    return result
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
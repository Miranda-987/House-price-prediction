

import util
util.load_saved_artifacts()

from flask import Flask,request,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})





@app.route('/get_location_names',methods=['GET','POST'])
def get_location_names():
    response=jsonify({
        'location':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    print("DATA:", data)

    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    try:
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        return jsonify({
            'estimated_price': estimated_price
        })

    except (KeyError, TypeError, ValueError) as e:
        return jsonify({"error": f"Invalid request data: {e}"}), 400

if __name__=='__main__':
    print("Starting Python Flask Server for home price prediction..")
    print(app.url_map)

    app.run()
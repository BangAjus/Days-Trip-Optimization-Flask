from flask import Flask, jsonify, request

from utils import model
from utils.processing import *
from utils.auth import auth
from utils.errors import errorsBp

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(errorsBp)

@app.route('/', methods=['GET'])
@auth.login_required
def get_server():
    return jsonify({
        "status" : {
            "code" : 200,
            "message" : "Welcome to the Back-End server of Day Trips Optimization!"
        },
        "data" : None
    }), 200

@app.route("/optimize", methods=['POST'])
@auth.login_required
def index():
    data = request.json
    features, loc_name = process_data_after_json(data)
    features_scaled = min_max_scaling(features)

    labels, coloring = model.clustering(features_scaled,
                                        int(data['days']))
    labels = labels.reshape(-1, 1)
    coloring = coloring.reshape(-1, 1)
    
    features = concatenate((features, labels),
                        axis=1)
    features = concatenate((features, coloring),
                        axis=1)

    return jsonify({"status":{
                        "code":200,
                        "message":"Success fetching the API"
                        },
                        
                    "data":[{'latitude':i,
                    'longitude':j,
                    'label':k,
                    'color':l,
                    'location_name': loc_name} \
                    for i, j, k, l, loc_name in \
                        zip(features[:, 0],
                            features[:, 1],
                            features[:, 2],
                            features[:, 3],
                            loc_name)]
                })

from flask import Flask, jsonify, request
from flask_cors import CORS

from apps.errors import errorsBp
from apps.auth import auth

from utils import model
from utils.processing import *
import os

port = int(os.environ.get("PORT", 10111))
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

@app.route("/api", methods=["GET"])
@auth.login_required
def process_data():
        
    data = request.json
    features = process_data_after_json(data)
    features_scaled = min_max_scaling(features)

    labels, coloring = model.clustering(features_scaled,
                                        int(data['days']))
    labels = labels.reshape(-1, 1)
    coloring = coloring.reshape(-1, 1)
    
    features = concatenate((features, labels),
                        axis=1)
    features = concatenate((features, coloring),
                        axis=1)

    return jsonify({
        "status" : {
            "code":200,
            "message":"Success fetching the API!"
        },
                        
        "data":[{'latitude':i,
                'longitude':j,
                'label':k,
                'color':l} \
                for i, j, k, l in \
                    zip(features[:, 0],
                        features[:, 1],
                        features[:, 2],
                        features[:, 3])]
    }), 200
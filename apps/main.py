from flask import Flask, jsonify, request

from utils import model
from utils.processing import *

app = Flask('ML_API')

@app.route("/", methods=["GET"])
def index():

    if not request:
        return jsonify({"status":
                        { "code": 400,
                          "message":"Couldn't fetch the API"
                               }
                    },
                    400)
    data = request.json
    features = process_data_after_json(data)
    features_scaled = min_max_scaling(features)

    labels = model.clustering(features_scaled,
                              int(data['days']))
    labels = labels.reshape(-1, 1)
    
    features = inverse_scaling(features)
    features = concatenate((features, labels),
                           axis=1)

    return jsonify({"status":{
                        "code":200,
                        "message":"Success fetching the API"
                        },
                        
                    "data":[{'latitude':i,
                             'longitude':j,
                             'label':k} \
                             for i, j, k in \
                                 zip(features[:, 0],
                                     features[:, 1],
                                     features[:, 2])]
                   })
from flask import Flask, render_template, make_response, jsonify, request
from flask_cors import CORS

from movie_recommender import get_recommendations, random_recommendation, data

app = Flask(__name__)
CORS(app)


HOST = '0.0.0.0'
PORT = '3200' 

# @app.route('/')
# def user_recommendations():
#     if request.args:
#         req = request.args
#         res = {}
#         for key, value in req.items():
#             res[key] = value
#         res = make_response(jsonify(res), 200)
#         return res

#     res = make_response(jsonify({ "error": "No user provided" }), 400)
#     return res

@app.route('/<id>', methods=["POST"])
def user_recommendations(id):
    req = request.get_json()

    if id not in data:
        data.update({ id: req })

    res = make_response(jsonify({ "tmdbId": random_recommendation(data, id) }), 200)
    return res

if __name__ == '__main__':
    print(f"Running in port {PORT}")
    app.run(host=HOST, port=PORT)
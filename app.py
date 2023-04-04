from flask import Flask, request, jsonify
from recom import recommend

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_movie_recommendation():
    title = request.args.get('title')
    if not title:
        return 'Please provide a title using the "title" query parameter.'

    recommendation = recommend(title)
    response = {"Movies": recommendation}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

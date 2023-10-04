from flask import Flask, g, jsonify
import requests
import json
from score import ScoreMap

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"Success": "OK"}), 200

def get_data():
    url = 'https://www.canada.ca/content/dam/ircc/documents/json/ee_rounds_123_en.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get('rounds', [])
        g.data = data
        return data
    except requests.RequestException as e:
        app.logger.error(f"Error fetching data from {url}: {e}")
        return None

@app.route('/rank/<score>', methods=['GET'])
def get_approx_rank(score):
    try:
        score = int(score)
        if not(0 <= score and score <= 1200):
            raise ValueError("Score must be within 0 - 1200")
    except ValueError as ve:  # Catch exceptions raised by invalid input or manual raise
        app.logger.error(f"Error: {str(ve)}.")
        return jsonify({"error": str(ve)}), 400  # Returns a 400 Bad Request response with error message
    data = getattr(g, 'data', None)
    if data is None:
        get_data()
        data = g.data
    if len(data) > 1:
        latest_score_json = data[0]
    current_score = ScoreMap(latest_score_json)
    return str(current_score.calculate_approx_rank(int(score)))

if __name__ == '__main__':
    app.run(debug=True)
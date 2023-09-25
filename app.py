from flask import Flask, render_template
import requests
import json
from score import ScoreMap

app = Flask(__name__)

@app.route('/')
def home():

    filename = 'data.json'

    #url = 'https://www.canada.ca/content/dam/ircc/documents/json/ee_rounds_123_en.json'  # Replace with the actual URL
    try:
        #response = requests.get(url)
        #return render_template('index.html', data=data)
        with open(filename, 'r') as file:
            data = json.load(file)
        currentScore = ScoreMap(data['rounds'][0])
        return ScoreMap.getRange(423)

    except Exception as e:
        print(f"Error fetching data: {e}")
        return "Internal Server Error", 500


if __name__ == '__main__':
    app.run(debug=True)
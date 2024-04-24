from flask import Flask, render_template, jsonify
from requests import get

app = Flask(__name__)

@app.route('/scores', methods=['GET'])
def get_scores():
    try:
        response = get("http://193.164.149.85:5000/scores")
        result = response.json()
        return jsonify(result[0])
    except Exception as e:
        print(e)
        return jsonify({"error": "Error fetching data"})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

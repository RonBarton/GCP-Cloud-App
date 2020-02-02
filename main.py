from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'This is Project 1 for Cloud computing 455658655 '

@app.route('/noah')
def bob():
    val = {"value": "Noah is gheyfish"}
    return jsonify(val)

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
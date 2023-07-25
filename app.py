# save this as app.py
import subprocess
from flask import Flask,jsonify,make_response
from src.etl.factory import create_etl


app = Flask(__name__)

@app.route("/zona_sul")
def run_zona_sul():
    etl = create_etl('zona_sul')
    etl.run()
    return make_response(jsonify('ETL Concluído!'))

@app.route("/prix")
def run_prix():
    etl = create_etl('prix')
    etl.run()
    return make_response(jsonify('ETL Concluído!'))

@app.route('/staging')
def run_staging():
    subprocess.run(['bash', 'datalake/routes/route_staging.sh'], check=True)
    return make_response(jsonify('ETL Concluído!'))

@app.route('/marts')
def run_marts():
    subprocess.run(['bash', 'datalake/routes/route_staging.sh'], check=True)
    return make_response(jsonify('ETL Concluído!'))

app.run(host='0.0.0.0', port=5000)
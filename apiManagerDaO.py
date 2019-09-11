__author__ = 'utkarsh_raghav'
from flask import Flask, jsonify
from dataAccessLayer import DataAccessLayer
import sqlite3
import logging


app = Flask(__name__)
data_access_object = DataAccessLayer()


@app.route('/last_known_locations', methods=['GET'])
def last_known_locations():
    rows = data_access_object.fetch_last_known_locations_data()
    json = jsonify(rows)
    return json

@app.route('/last_known_locations/<int:num>', methods=['GET'])
def last_known_n_locations(num):
    rows = data_access_object.fetch_last_known_n_location_data(num)
    json = jsonify(rows)
    return json

@app.route('/pass_by_times/<int:num>', methods=['GET'])
def fetch_pass_by_time(num):
    rows = data_access_object.fetch_last_known_n_location_data(num)
    json = jsonify(rows)
    return json

@app.route('/pass_by_times', methods=['GET'])
def fetch_pass_by_n_times():
    rows = data_access_object.fetch_last_known_locations_data()
    json = jsonify(rows)
    return json


if __name__ == '__main__':
    logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)

    app.run(debug=True)

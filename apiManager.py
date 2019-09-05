__author__ = 'utkarsh_raghav'
from flask import Flask, jsonify
import sqlite3
import logging


app = Flask(__name__)

@app.route('/last_known_locations', methods=['GET'])
def last_known_locations():
    with sqlite3.connect("APIData.db") as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM ApiDataTableDemo")
        rows = c.fetchall()
        json = jsonify(rows)
        c.close()
    return json

@app.route('/last_known_locations/<int:num>', methods=['GET'])
def last_known_n_locations(num):
    with sqlite3.connect("APIData.db") as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM ApiDataTableDemo")
        rows = c.fetchmany(num)
        json = jsonify(rows)
        c.close()
    return json

@app.route('/pass_by_times/<int:num>', methods=['GET'])
def n_pass_by_times(num):
    with sqlite3.connect("APIData.db") as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM PassbyDataTableDemo")
        rows = c.fetchmany(num)
        json = jsonify(rows)
        c.close()
    return json

@app.route('/pass_by_times', methods=['GET'])
def pass_by_times():
    with sqlite3.connect("APIData.db") as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM PassbyDataTableDemo")
        rows = c.fetchall()
        json = jsonify(rows)
        c.close()
    return json


if __name__ == '__main__':
    logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)

    app.run(debug=True)

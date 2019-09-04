__author__ = 'utkarsh_raghav'
from flask import Flask, jsonify
import sqlite3


app = Flask(__name__)

@app.route('/last_known_locations', methods=['GET'])
def last_know_locations():
    with sqlite3.connect("APIData.db") as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM ApiDataTableDemo")
        rows = c.fetchall()
        print(rows)
        json = jsonify(rows)
        c.close()
    return json

@app.route('/pass_by_times', methods=['GET'])
def pass_by_times():
    with sqlite3.connect("APIData.db") as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM PassbyDataTableDemo")
        rows = c.fetchall()
        print(rows)
        json = jsonify(rows)
        c.close()
    return json


if __name__ == '__main__':
    app.run(debug=True)

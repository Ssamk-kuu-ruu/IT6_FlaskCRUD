from flask import Flask, make_response, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'Happyeveryday0519**'
app.config["MYSQL_DB"] = 'finalproj'


app.config["MYSQL_CURSORCLASS"] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def hello_world():
    return "<p> Hello World </p>"

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    return data

@app.route("/persons", methods=["GET"])
def get_persons():
    data = data_fetch(""" SELECT * FROM persons """)

    return make_response(jsonify(data), 200)

@app.route("/persons/<int:id>", methods=["GET"])
def get_persons_by_id(id):
    data = data_fetch (""" SELECT * FROM persons WHERE personid = {} """.format(id))
    return make_response(jsonify(data), 200)



if __name__ == "__main__":
    app.run(debug=True)

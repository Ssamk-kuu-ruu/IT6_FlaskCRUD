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

@app.route("/tbl_products", methods=["GET"])
def get_products():
    cur = mysql.connection.cursor()
    query = """
    SELECT * FROM tbl_products
    """

    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    return make_response(jsonify(data), 200)

if __name__ == "__main__":
    app.run(debug=True)

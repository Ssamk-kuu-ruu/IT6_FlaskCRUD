from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Happyeveryday0519**"
app.config["MYSQL_DB"] = "finalproj"


app.config["MYSQL_CURSORCLASS"] = "DictCursor"

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


@app.route("/persons", methods=["POST"])
def add_persons():
    cur = mysql.connection.cursor()
    info = request.get_json()

    name = info["Name"]
    age = info["Age"]
    email = info["Email"]

    cur.execute(
        """
            INSERT INTO persons (Age, Email, Name) VALUES (%s, %s, %s)
    """,
        (age, email, name),
    )
    mysql.connection.commit()
    print("row(s) affected {}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()

    return make_response(
        jsonify(
            {"message": "person added successfully", "rowsaffected": rows_affected}
        ),
        201,
    )


@app.route("/persons/<int:id>", methods=["GET"])
def get_persons_by_id(id):
    data = data_fetch(""" SELECT * FROM persons WHERE personid = {} """.format(id))
    return make_response(jsonify(data), 200)


@app.route("/persons./<int:id>", methods=["PUT"])
def update_person(id):
    cur = mysql.connection.cursor()
    info = request.get_json()

    name = info["Name"]
    age = info["Age"]
    email = info["Email"]

    cur.execute(
        """
        UPDATE persons SET Age = %s, Email = %s, Name = %s WHERE personid = %s
    """,
        (age, email, name, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()

    return make_response(
        jsonify(
            {"message": "person updated successfully", "rowsaffected": rows_affected}
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)

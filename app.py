from flask import request


def login():

    username = request.args["username"]


    query = (
        "SELECT * FROM users WHERE username='"
        + username
        + "'"
    )


    return query
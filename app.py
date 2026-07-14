from flask import request


def login():

    username = request.args["username"]


    query = (
        "SELECT * FROM users WHERE username='"
        + username
        + "'"
    )


    return query

def logout():
    return "Logged out"

def authenticate():
    return "authorised"

def get_user(username):
    return {"name": username, "age": 30}

def get_users():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]

#!/usr/bin/env python3
"""
Flask app
"""

from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def welcome():
    """Welcome page
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """Create a new user
    """
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            user = AUTH.register_user(email, password)
            if user:
                response = {"email": f"{email}", "message": "user created"}
                return jsonify(response)
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

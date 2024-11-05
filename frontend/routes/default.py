from os import getenv
from requests import get
from flask import render_template
from flask_login import current_user, login_required
from .. import app


BACKEND_URL = getenv("BACKEND_URL")


@app.get("/")
@login_required
def index():
    gmail = current_user.email
    data = {
        "email": gmail
    }
    transactions = {
        "transactions": get(f"{BACKEND_URL}/read", json=data).json()
    }
    print(" * " * 80)
    print(transactions.get("transactions"))
    return render_template("index.html", **transactions) 



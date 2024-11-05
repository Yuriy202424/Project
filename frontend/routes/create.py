from os import getenv
from datetime import datetime

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from requests import post

from .. import app


BACKEND_URL = getenv("BACKEND_URL")

@app.get('/create')
@login_required
def create():
    return render_template('create.html')


@app.post('/create')
@login_required
def create_transaction():
    """ this function gets values from html, adds them to data and sends it to backend """
    owner = current_user.email
    amount = request.form.get("amount")
    description = request.form.get("description")
    category = request.form.get("category")
    full_date = str(datetime.now())
    date = full_date[:16]
    data = {'owner' : owner, 'amount' : amount, 'description' : description, 'category' : category, "date" : date}
    response = post(f"{BACKEND_URL}/create", json=data)
    if response.status_code==201:
        return redirect(url_for('index'))
    else: 
        code = response.status_code
        text = response.text
        return render_template("errors.html", code=code, text=text)
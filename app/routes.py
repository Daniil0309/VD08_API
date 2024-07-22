from flask import render_template, request
import requests
from app import app

@app.route('/')
def quote():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    return render_template('quote.html', quote=data['content'], author=data['author'])
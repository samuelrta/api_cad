from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config ['TITLE'] = "pontocad"

Bootstrap(app)


@app.route("/")
def index():
    products = ['Cabelo', 'Varba', 'Cerveja']
    return render_template('index.html', products=products)


app.run(debug=True, use_reloader=True)

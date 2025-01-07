from flask import Flask, render_template
import random

app: Flask = Flask(__name__)

@app.route("/")
def home() -> str: 
    nomi: list[str] = ["christian", "marco", "franco"]
    index: int= random.randint(0,2)
    return render_template("home.html",titolo="Welcome", nome=nomi[index])

@app.route("/details")
def details() -> str:
    prodottiTupla: tuple[tuple] = (("birra", 33, 2.5 ), ("pasta", 11, 0.80))
    return render_template("details.html", titolo="details", pageName="product list:" , prodotti=prodottiTupla)






####################################################
app.run(debug=True) 
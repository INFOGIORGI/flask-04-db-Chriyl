from flask import Flask, render_template
from flask_mysqldb import MySQL
import random
"""
IP: 138.41.20.102
PORTA: 53306
DB: w3schools
USERNAME: ospite
PASSWORD: ospite

"""
app = Flask(__name__)

app.config["MYSQL_HOST"] = "138.41.20.102"
app.config["MYSQL_PORT"] = 53306
app.config["MYSQL_USER"] = "ospite"
app.config["MYSQL_PASSWORD"] = "ospite"
app.config["MYSQL_DB"] = "w3schools"

Mysql= MySQL(app)

@app.route("/") # specifico il path della url
def home() -> str: # funzione che viene richiamata al raggiungimento di http://0.0.0.0:5000/
    return render_template("home.html", titolo="home", header="Home")



@app.route("/products")
def products() -> str:
    cursor = Mysql.connect.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    dati: (tuple) = cursor.fetchall()
    
    return render_template("products.html", products = dati)



@app.route("/category/<id>")
def category(id) -> str:
    #numero = input()
    cursor = Mysql.connect.cursor()
    query = "SELECT * FROM categories WHERE CategoryId = %s"
    cursor.execute(query, id)
    dati: (tuple) = cursor.fetchall() 

    return render_template("category.html", titolo="category", header='category' , category=dati)


 

####################################################
app.run(debug=True) # il debug serve per apportare le modifiche senza re-runnare il server (molto fico non lo sapevo)
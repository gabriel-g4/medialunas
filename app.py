from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
database = "medialunas.db"

# with sqlite3.connect(database) as connection:
#     connection.execute("INSERT INTO medialunas (dia, mes, anio, cantidad, tipo)\
#                         VALUES (?, ?, ?, ?, ?)", (13, 6, 2024, 12, "practica"))

# with sqlite3.connect(database) as connection:
#     connection.execute(".schema")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
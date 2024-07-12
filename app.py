from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
database = "medialunas.db"
COLUMNAS_MEDIALUNAS = ["id", "cantidad", "tiempo_descanso", "tiempo_coccion", "costo_c_una"\
                       , "cantidad_vendida", "precio_c_una", "ganancia", "tipo", "masa_madre"\
                        , "fecha"]

@app.route('/')
def index():
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medialunas")
        data = cursor.fetchall()
    print(data)
    return render_template("index.html", medialunas=data\
                           , columnas_medialunas=COLUMNAS_MEDIALUNAS)

if __name__ == "__main__":
    app.run()
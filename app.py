from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
database = "medialunas.db"
with sqlite3.connect(database) as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT c.name FROM pragma_table_info('medialunas') c")
    columnas_medialunas = cursor.fetchall()

for i in range(len(columnas_medialunas)):
    columnas_medialunas[i] = columnas_medialunas[i][0]
    


@app.route('/')
def index():
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medialunas")
        data = cursor.fetchall()
    return render_template("index.html", medialunas=data\
                           , columnas_medialunas=columnas_medialunas)

@app.route('/medialunas/<int:id>')
def mostrar_medialunas(id: int):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medialunas WHERE id=?", (str(id)))
        selected_medialuna = cursor.fetchall()

    medialuna = {}
    for i in range(len(columnas_medialunas)):
        medialuna[columnas_medialunas[i]] = selected_medialuna[0][i]


    return render_template("medialunas.html", medialuna=medialuna)


if __name__ == "__main__":
    app.run()
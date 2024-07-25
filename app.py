from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
database = "medialunas.db"

with sqlite3.connect(database) as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT c.name FROM pragma_table_info('medialunas') c")
    COLUMNAS_MEDIALUNAS = cursor.fetchall()
    cursor.execute("SELECT c.name FROM pragma_table_info('ingredientes') c")
    COLUMNAS_INGREDIENTES_PRECIOS = cursor.fetchall()

for i in range(len(COLUMNAS_MEDIALUNAS)):
    COLUMNAS_MEDIALUNAS[i] = COLUMNAS_MEDIALUNAS[i][0]
    
for i in range(len(COLUMNAS_INGREDIENTES_PRECIOS)):
    COLUMNAS_INGREDIENTES_PRECIOS[i] = COLUMNAS_INGREDIENTES_PRECIOS[i][0]
    


@app.route('/')
def index():
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medialunas")
        data = cursor.fetchall()
    return render_template("index.html", medialunas=data\
                           , columnas_medialunas=COLUMNAS_MEDIALUNAS)

@app.route('/medialunas/<int:id>')
def mostrar_medialunas(id: int):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medialunas WHERE id=?", (str(id),))
        selected_medialuna = cursor.fetchone()
        cursor.execute("SELECT * FROM ingredientes WHERE id=?", (str(id),))
        selected_ingredientes = cursor.fetchone()
        cursor.execute("SELECT * FROM precios WHERE id=?", (str(id),))
        selected_precios = cursor.fetchone()
    
    print(COLUMNAS_INGREDIENTES_PRECIOS)

    medialuna = {}
    ingredientes = {}
    precios = {}

    if selected_medialuna != None:
        for i in range(len(COLUMNAS_MEDIALUNAS)):
            medialuna[COLUMNAS_MEDIALUNAS[i]] = selected_medialuna[i]
    if selected_ingredientes != None:
        for i in range(len(COLUMNAS_INGREDIENTES_PRECIOS)):
            ingredientes[COLUMNAS_INGREDIENTES_PRECIOS[i]] = selected_ingredientes[i]
    if selected_precios != None:
        for i in range(len(COLUMNAS_INGREDIENTES_PRECIOS)):
            precios[COLUMNAS_INGREDIENTES_PRECIOS[i]] = selected_precios[i]


    return render_template("medialunas.html", medialuna=medialuna, 
                           ingredientes=ingredientes, precios=precios)


if __name__ == "__main__":
    app.run()
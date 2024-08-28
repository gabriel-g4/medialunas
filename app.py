from flask import Flask, render_template, redirect, request
import sqlite3
from funciones import crear_diccionario
from datetime import datetime

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
        cursor.execute("SELECT * FROM medialunas ORDER BY id DESC")
        data = cursor.fetchall()

    return render_template("index.html", medialunas=data\
                           , columnas_medialunas=COLUMNAS_MEDIALUNAS)


@app.route('/agregar', methods=["GET", "POST"])
def agregar():
    if request.method == "GET":
        return render_template("agregar.html", columnas_medialunas=COLUMNAS_MEDIALUNAS
                           , columnas_ingredientes_precios=COLUMNAS_INGREDIENTES_PRECIOS[1:])
    elif request.method == "POST":

        cantidad = request.form.get("cantidad")
        tiempo_descanso = request.form.get("tiempo_descanso")
        tiempo_coccion = request.form.get("tiempo_coccion")
        costo_c_una = request.form.get("costo_c_una")
        cantidad_vendida = request.form.get("cantidad_vendida")
        precio_c_una = request.form.get("precio_c_una")
        ganancia = request.form.get("ganancia")
        tipo = request.form.get("tipo")
        masa_madre = request.form.get("masa_madre")
        
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO medialunas (cantidad, tiempo_descanso\
                           , tiempo_coccion, costo_c_una, cantidad_vendida, precio_c_una, \
                           ganancia, tipo, fecha, masa_madre) VALUES (?,?,?,?,?,?,?,?, \
                           ? ,?)",
                            (cantidad, tiempo_descanso, tiempo_coccion, costo_c_una,
                             cantidad_vendida, precio_c_una, ganancia, tipo, datetime.now() , masa_madre))
        return redirect("/")
            


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

    medialuna = crear_diccionario(COLUMNAS_MEDIALUNAS, selected_medialuna)
    ingredientes = crear_diccionario(COLUMNAS_INGREDIENTES_PRECIOS, selected_ingredientes)
    precios = crear_diccionario(COLUMNAS_INGREDIENTES_PRECIOS, selected_precios)

    return render_template("medialunas.html", medialuna=medialuna, 
                           ingredientes=ingredientes, precios=precios)


if __name__ == "__main__":
    app.run()
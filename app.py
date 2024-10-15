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
        return render_template("agregar.html",
                           columnas_ingredientes_precios=COLUMNAS_INGREDIENTES_PRECIOS[1:], medialuna="", ingredientes="", precios="", titulo="Agregar", boton="Agregar", action="agregar")
    
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
        texto = request.form.get("texto")

        harina = request.form.get("harina")
        levadura = request.form.get("levadura")
        azucar = request.form.get("azucar")
        miel = request.form.get("miel")
        sal = request.form.get("sal")
        leche = request.form.get("leche")
        huevos = request.form.get("huevos")
        manteca = request.form.get("manteca")

        precio_harina = request.form.get("precio_harina")
        precio_levadura = request.form.get("precio_levadura")
        precio_azucar = request.form.get("precio_azucar")
        precio_miel = request.form.get("precio_miel")
        precio_sal = request.form.get("precio_sal")
        precio_leche = request.form.get("precio_leche")
        precio_huevos = request.form.get("precio_huevos")
        precio_manteca = request.form.get("precio_manteca")

        
        
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO medialunas (cantidad, tiempo_descanso\
                           , tiempo_coccion, costo_c_una, cantidad_vendida, precio_c_una, \
                           ganancia, tipo, creacion, masa_madre, texto, ultima_modificacion) VALUES (?,?,?,?,?,?,?,?, \
                           ? ,?,?,?)",
                            (cantidad, tiempo_descanso, tiempo_coccion, costo_c_una,
                             cantidad_vendida, precio_c_una, ganancia, tipo, datetime.now() , masa_madre, texto, datetime.now()))
            
            # Tomar el id de la medialuna insertada en Medialunas.

            cursor.execute("SELECT id FROM medialunas ORDER BY creacion DESC")
            id = cursor.fetchone()[0]

            # añadir entrada a ingredientes
           
            cursor.execute("INSERT INTO ingredientes (id, harina, levadura, azucar, miel, sal,\
                           leche, huevos, manteca) VALUES (?,?,?,?,?,?,?,?,?)",
                           (id, harina, levadura, azucar, miel, sal, leche, huevos, manteca))
            
            # añadir entrada a precios

            cursor.execute("INSERT INTO precios (id, harina, levadura, azucar, miel, sal,\
                           leche, huevos, manteca) VALUES (?,?,?,?,?,?,?,?,?)",
                           (id, precio_harina, precio_levadura, precio_azucar, precio_miel, 
                            precio_sal, precio_leche, precio_huevos, precio_manteca))
            
        return redirect("/")
            

@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar(id: int):

    if request.method == "GET":

        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            
            cursor.execute("SELECT * FROM medialunas WHERE id=?", (str(id),))
            selected_medialuna = cursor.fetchone()

            cursor.execute("SELECT * FROM ingredientes WHERE id=?", (str(id),))
            selected_ingredientes = cursor.fetchone()

            cursor.execute("SELECT * FROM precios WHERE id=?", (str(id),))
            selected_precios = cursor.fetchone()
        
        medialuna = crear_diccionario(COLUMNAS_MEDIALUNAS, selected_medialuna)
        ingredientes = crear_diccionario(COLUMNAS_INGREDIENTES_PRECIOS, selected_ingredientes)
        precios = crear_diccionario(COLUMNAS_INGREDIENTES_PRECIOS, selected_precios)
        
        return render_template("agregar.html", columnas_ingredientes_precios=COLUMNAS_INGREDIENTES_PRECIOS[1:],
                            medialuna=medialuna, ingredientes=ingredientes, precios=precios, titulo="Editar Medialunas Nº:" + str(id),
                            boton="Guardar", action="editar/" + str(id))
    
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
        texto = request.form.get("texto")

        harina = request.form.get("harina")
        levadura = request.form.get("levadura")
        azucar = request.form.get("azucar")
        miel = request.form.get("miel")
        sal = request.form.get("sal")
        leche = request.form.get("leche")
        huevos = request.form.get("huevos")
        manteca = request.form.get("manteca")

        precio_harina = request.form.get("precio_harina")
        precio_levadura = request.form.get("precio_levadura")
        precio_azucar = request.form.get("precio_azucar")
        precio_miel = request.form.get("precio_miel")
        precio_sal = request.form.get("precio_sal")
        precio_leche = request.form.get("precio_leche")
        precio_huevos = request.form.get("precio_huevos")
        precio_manteca = request.form.get("precio_manteca")

        
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE medialunas SET cantidad=?, tiempo_descanso=?\
                           , tiempo_coccion=?, costo_c_una=?, cantidad_vendida=?, precio_c_una=?, \
                           ganancia=?, tipo=?, ultima_modificacion=?, masa_madre=?, texto=? WHERE id = ?",
                            (cantidad, tiempo_descanso, tiempo_coccion, costo_c_una,
                             cantidad_vendida, precio_c_una, ganancia, tipo, datetime.now() , masa_madre, texto,
                             str(id)))
            
            # añadir entrada a ingredientes
           
            cursor.execute("UPDATE ingredientes SET harina=?, levadura=?, azucar=?, miel=?, sal=?,\
                           leche=?, huevos=?, manteca=? WHERE id = ?",
                           (harina, levadura, azucar, miel, sal, leche, huevos, manteca, str(id)))
            
            # añadir entrada a precios

            cursor.execute("UPDATE precios SET harina=?, levadura=?, azucar=?, miel=?, sal=?,\
                           leche=?, huevos=?, manteca=? WHERE id = ?",
                           (precio_harina, precio_levadura, precio_azucar, precio_miel, precio_sal, precio_leche, precio_huevos, precio_manteca, str(id)))
            
        return redirect("/")


@app.route('/eliminar/<int:id>')
def eliminar(id: int):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM medialunas WHERE id = ?", (int(id),))
        cursor.execute("DELETE FROM ingredientes WHERE id = ?", (int(id),))
        cursor.execute("DELETE FROM precios WHERE id = ?", (int(id),))
    return redirect('/')



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
    

    medialuna = crear_diccionario(COLUMNAS_MEDIALUNAS, selected_medialuna)
    ingredientes = crear_diccionario(COLUMNAS_INGREDIENTES_PRECIOS, selected_ingredientes)
    precios = crear_diccionario(COLUMNAS_INGREDIENTES_PRECIOS, selected_precios)

    return render_template("medialunas.html", medialuna=medialuna,
                           ingredientes=ingredientes, precios=precios)


if __name__ == "__main__":
    app.run()
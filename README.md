# Medialunas - CS50 final project

Hi! My name is **Gabriel García**, I am from **Buenos Aires, Argentina**, and this is my CS50x final project: **_Medialunas_**.

* Video demo: [here](https://youtu.be/QGPKzUTrugc)
* Edx username: **gabriel_g4**
* GitHub username: **gabriel-g4**

## Goals

The project is intended to be a CRUD and administration local app for my girlfriend's bakery.

The main purpose is to archive information of her production in a database, quickly search it and visualize it in a simple and rather aesthetic way.


## Breakdown

**Technologies used**: Python, Flask, Jinja2, HTML, CSS, Bootstrap, Javascript, Git, SQLite3

I chose Python and specifically the Flask framework, because we used it in the course and I was already familiar with it. SQLite was chosen for the same reasons, and because it is a very simple app, and doesn't need a lot of scalability.
For the HTML, I used a layout file and extended it to all the other HTML files, containing the same headers and footer. 
For the CSS, I preferred to use Bootstrap for convenience, although I used custom CSS too.
I used Javascript with no other framework.

### Endpoints

* ### / (index)

    The index page. It fetches the database's 'medialunas' table and shows all tuples in a main table. If you click on one of its rows, it will send you to [_/detalle/:id_](#detalleid).
    You can add an entry to the database clicking the **(Agregar)** button just above the main table. It will send you to [_/agregar_](#agregar).

    __index.js__: Adds a click event to each main table's row to go to its detalle's url.

    It has a "dynamic" search bar that operates in conjuction with a select option. By default, this select option is empty. So, if you type in the search input, it will do a general search of the value in all the database table's columns and modify the main table only showing matching rows. You can also search by specific column, selecting its correspondent option.

    __index.js__ dynamic search bar: My approach to this problem was to get the main table, and operate on its rows and cells. I used an event on the keyup of the bar, then that bar value is stored and later compared to each row value, accesing it by its index. The select tag and its options must have the same order as the table columns. (not the same values).
    If the table in its accessed cell includes the search bar's value shows the row, else changes its style.display to none.
    If there is an extra value at the start of the select tag (the general search), so I need to extract 1 to match the table's columns' length.
    In case the option "-" is selected, it performs a general search in all rows and columns.
    When there's a search in an specific column it doesn't need to go through all the values stored in the row, because I have the filter index stored.

* ### /agregar
  
    A form that lets you insert into the database. It has an HTML validation on all the necessary inputs. When you click 'Guardar', it saves the values and redirects you to the [index _/_](#-index).

* ### /detalle/:id

    Shows all the detailed information for the item with the  _:id_ value. The information is displayed in two separate tables, and in the top of the page you have a button to edit (goes to [_/editar/:id_](#editarid)) and other to delete (goes to [_/eliminar/:id_](#eliminarid)) this item. Deleting requires a confirmation.

    __detalle.js__ on delete button: Gives the delete button a click event with a confirmation and redirects.

* ### /editar/:id

    It renders the same form as [_/agregar_](#agregar), but this time the form's inputs are populated by the values of the item specified with the _:id_. You can change the current values and save it, and it will update the item in the database and redirect you to [index _/_](#-index).

    __agregar.js__ in _/editar_ mode: Changes select tags "tipo" and "masa_madre" by making the db fetched option the default "selected" option for convenience sake.

* ### /eliminar/:id

    Deletes the item with the specified _:id_ from the database.
  
>[!CAUTION]
>Visiting the link this way deletes instantly and doesn't require confirmation. It's intended to be used from [_/editar/:id_](#editarid).



### Database
Initialization: run the command 
```bash
python init_db.py
```
The database I created, based on her requirements and not knowing too much about relational databases and SQL. The relationship between tables are 1 to 1.
```sql
CREATE TABLE IF NOT EXISTS 'medialunas' (
                'id'    INTEGER NOT NULL UNIQUE,
                'cantidad'      INTEGER,
                'costo_c_una'   REAL,
                'cantidad_vendida'      INTEGER,
                'precio_c_una'  REAL,
                'ganancia'      REAL,
                'masa_madre' TEXT,
                'levado_minutos' INTEGER,
                'coccion_minutos' INTEGER,
                'creacion' TEXT,
                'texto' TEXT,
                'tipo'  TEXT,
                'ultima_modificacion' TEXT,
                PRIMARY KEY("id" AUTOINCREMENT));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE ingredientes (
                'id' INTEGER NOT NULL,
                'harina_000' INTEGER,
                'levadura' INTEGER,
                'azucar' INTEGER,
                'miel' INTEGER,
                'sal' INTEGER,
                'leche' INTEGER,
                'huevos' INTEGER,
                'manteca' INTEGER,
                FOREIGN KEY(id) REFERENCES medialunas(id));
CREATE TABLE precios (
                'id' INTEGER NOT NULL,
                'harina_000' INTEGER,
                'levadura' INTEGER,
                'azucar' INTEGER,
                'miel' INTEGER,
                'sal' INTEGER,
                'leche' INTEGER,
                'huevos' INTEGER,
                'manteca' INTEGER,
                FOREIGN KEY(id) REFERENCES medialunas(id));
```

## Special thanks to..

1. My girlfriend for all her advice and support.
2. All the CS50x staff, and especially David Malan for being a great teacher.
3. My university professors, that helped me indirectly to improve this project.

This project took me some months going in and off work and many times I felt stuck and didn't know what to do, but with effort I finished it as fast and as good as I could. This was CS50!

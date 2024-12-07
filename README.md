# Medialunas - CS50 final project

Hi! My name is **Gabriel García**, I am from **Buenos Aires, Argentina**, and this is my CS50x final project: **_Medialunas_**.

* Video demo: http://www.youtube.com
* Edx username: **gabriel_g4**
* GitHub username: **gabriel-g4**

## Goals

The project is intended to be a CRUD and administration web app for my girlfriend's bakery.

The main purpose is to archive information of her production in a database, quickly search it and visualize it in a simple and rather aesthetic way.


## Breakdown
**Technologies used**: Python, Flask, Jinja2, HTML, CSS, Bootstrap, Javascript, Git

* ### /
    <hr>
    The index page. It fetches the database's 'medialunas' table and shows all tuples in a main table. If you click on one of its rows, it will send you to _/detalle/:id_.
    You can add an entry to the database clicking the **(Agregar)** button just above the main table. It will send you to _/agregar_.

    It has a "dynamic" search bar that operates in conjuction with a select option. By default, this select option is empty. So, if you type in the search input, it will do a general search of the value in all the database table's columns and modify the main table only showing matching rows. You can also search by specific column, selecting its correspondent option.

* ### /agregar
    <hr>
    A form that lets you insert into the database. It has an HTML validation on all the necessary inputs. When you click 'Guardar', it saves the values and redirects you to the index _/_.

* ### /detalle/:id
    <hr>
    Shows all the detailed information for the item with the  _:id_ value. The information is displayed in two separate tables, and in the top of the page you have a button to edit (goes to _/editar/:id_) and other to delete (goes to _/eliminar/:id_) this item. Deleting requires a confirmation.

* ### /editar/:id
    <hr>
    It renders the same form as _/agregar_, but this time the form's inputs are populated by the values of the item specified with the _:id_. You can change the current values and save it, and it will update the item in the database and redirect you to index _/_.

* ### /eliminar/:id
    <hr>
    Deletes the item with the specified _:id_ from the database.
    >[!CAUTION]
    >Visiting the link this way deletes instantly and doesn't require confirmation. It's intended to be used from _/editar/:id_.

## Special thanks to

1. My girlfriend for all her advice and support.
2. All the CS50x staff, and especially David Malan for being a great teacher.

This project took me some months going in and off work and many times I felt stuck not knowing what to do, but with effort I finished it as fast and as good as I could. This was CS50! 
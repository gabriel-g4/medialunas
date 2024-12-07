import sqlite3

database = "medialunas.db"

with sqlite3.connect(database) as connection:
    try:
        cursor = connection.cursor()
        res = cursor.execute("SELECT name FROM sqlite_master")
        res = res.fetchall()

        if (res.count(("medialunas",)) and 
            res.count(("ingredientes",)) and 
            res.count(("precios",))):
            print("Tables are already created.")
            raise Exception
        
        cursor.execute("""
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
                       """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredientes ( 
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
                       """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS precios ( 
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
                       """)


        res = cursor.execute("SELECT name FROM sqlite_master")
        res = res.fetchall()
        
        if (res.count(("medialunas",))):
            print("Created table medialunas.")
        else:
            raise Exception("Error creating medialunas table.")
        
        if (res.count(("ingredientes",))):
            print("Created table ingredientes.")
        else:
            raise Exception("Error creating ingredientes table.")
        
        if (res.count(("precios",))):
            print("Created table precios.")
        else:
            raise Exception("Error creating precios table.")

    except Exception:
        print("Error ocurred.")
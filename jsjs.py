# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:20:36 2020

@author: palar
"""

import MySQLdb

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'MYDB' 

def run_query(query='select * from table'): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 

    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
    
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 

    return data

def upd():
    b1 = input("ID: ") 
    b2 = input("Nuevo valor: ") 
    query = "UPDATE table SET dato='%s' WHERE b1 = %i" % (b2, int(b1)) 
    run_query(query)

def insert():
    dato = input("Dato: ")
    query = "INSERT INTO table (dato) VALUES ('%s')" % dato
    run_query(query)
    
def eliminar():
    criterio = input("Ingrese criterio a eliminar coincidencias: ") 
    query = "DELETE FROM table WHERE dato = '%s'" % criterio 
    run_query(query)
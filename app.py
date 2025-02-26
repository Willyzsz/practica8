from flask import Flask

from flask import render_template
from flask import request
from flask import jsonify, make_response

import mysql.connector

import datetime
import pytz

from flask_cors import CORS, cross_origin

con = mysql.connector.connect(
    host="localhost",
    database="u338115605_basededatos",
    user="u338115605_base",
    password="Base_Datos5"
)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return render_template("index.html")

@app.route("/app")
def app2():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return "<h5>Hola, soy la view app</h5>"

@app.route("/clientes")
def clientes():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = "SELECT idCliente, nombreCliente, numero FROM cesar_awi_practica4_clientes LIMIT 10 OFFSET 0"
    cursor.execute(sql)
    registros = cursor.fetchall()

    return render_template("clientes.html", clientes=registros)

@app.route("/cuentas")
def cuentas():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = "SELECT * FROM cesar_awi_practica4_cuentas JOIN cesar_awi_practica4_clientes ON cesar_awi_practica4_cuentas.idCliente = cesar_awi_practica4_clientes.idCliente LIMIT 10 OFFSET 0 "

    cursor.execute(sql)
    registros = cursor.fetchall()

    # Si manejas fechas y horas

    for registro in registros:
        fechaHora = registro["fechaHora"]

        registro["fechaHora"] = fechaHora.strftime("%Y-%m-%d %H:%M:%S")
        registro["Fecha"]      = fechaHora.strftime("%d/%m/%Y")
        registro["Hora"]       = fechaHora.strftime("%H:%M:%S")

    return render_template("cuentas.html", cuentas=registros)


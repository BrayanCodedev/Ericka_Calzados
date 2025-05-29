from flask import Flask, render_template
import sqlite3
from models import Product

# Conexión global a la base de datos (en producción se recomienda manejar la conexión por petición)
conexion = sqlite3.connect("DB_EC.db", check_same_thread=False)

app = Flask(__name__)

@app.route('/')
def index():
    products = Product.get_all(conexion)
    return render_template('index.html', data={"products": products})

@app.route('/productos')
def productos():
    products = Product.get_all(conexion)
    return render_template('productos.html', data={"products": products})

@app.route('/login')
def login():
    # Normalmente no necesitas productos aquí, pero si quieres los pasas igual
    return render_template('login.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

if __name__ == '__main__':
    app.run(debug=True, port=8001)

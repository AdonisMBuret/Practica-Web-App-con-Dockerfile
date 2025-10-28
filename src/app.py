from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        # Obtener variables de entorno de Docker Compose
        db_host = os.environ.get('DB_HOST', 'db')  # 'db' es el nombre del servicio en docker-compose
        db_user = os.environ.get('DB_USER', 'root')
        db_password = os.environ.get('DB_PASSWORD', 'rootpassword')
        db_name = os.environ.get('DB_NAME', 'mydatabase')

        # Conectar a MySQL
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        db_version = cursor.fetchone()[0]
        cursor.close()
        conn.close()

        return f"Hola Mundo! Conectado a MySQL versión: {db_version}"
    except mysql.connector.Error as err:
        return f"Hola Mundo! Error al conectar a la BD: {err}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
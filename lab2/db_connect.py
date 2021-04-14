import mysql.connector
from mysql.connector import Error

def connect_db():
    try:

        connection = mysql.connector.connect( host="localhost", user="root", password="" , buffered=True)

        if connection.is_connected():

            cursor = connection.cursor()

            #create database 
            cursor.execute("CREATE  DATABASE IF NOT EXISTS python_lab2")

            #use created database
            cursor.execute("USE python_lab2")
            #create table employees
            cursor.execute("CREATE TABLE IF NOT EXISTS employees (id int unique not null AUTO_INCREMENT, email VARCHAR(255),work_mood VARCHAR(255), salary int(20), is_manager BOOLEAN, full_name VARCHAR(255), money int(20), sleep_mood VARCHAR(255), health_rate int(25) )")
            cursor.execute("select database();")

            return connection

    except Error as e:
        print("Error while connecting to MySQL", e)


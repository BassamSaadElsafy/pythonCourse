import mysql.connector
from mysql.connector import Error


def connect_db():
    try:

        connection = mysql.connector.connect( host="localhost", user="root", password="" )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()

            #create database 
            cursor.execute("CREATE  DATABASE IF NOT EXISTS python_lab2")

            #use created database
            cursor.execute("USE python_lab2")
            #create table employees
            cursor.execute("CREATE TABLE IF NOT EXISTS employees (id int unique not null AUTO_INCREMENT, email VARCHAR(255),work_mood VARCHAR(255), salary int(20), is_manager BOOLEAN, full_name VARCHAR(255), money int(20), sleep_mood VARCHAR(255), health_rate int(25) )")

            # cursor.execute("INSERT INTO `employees` (`id`, `email`, `salary`, `is_manager`, `full_name`, `money`, `sleep_mood`, `health_rate`) VALUES (4,'bassam@yahoo.com', 2500, 0, 'Bassam Saad', 3000, 'mood_what', 80)")


            # connection.commit()                           #should commit your changes to apply them to database

            cursor.execute("select database();")

            record = cursor.fetchone()

            # print("You're connected to database: ", record)

            return connection

    except Error as e:
        print("Error while connecting to MySQL", e)
    # finally:
    #     if connection.is_connected():
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")

from db_connect import*
from Employee import Employee
class Office:
    
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees():
        print("//====(Employees Information)===//")

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute('select * from employees')
        rows = cursor.fetchall()

        print("id-----  email--work_mood---salary--is_manager")
        for row in rows:
            # print(row)
            if row[4] == 0:
                print(row[0],"----", row[1], '----', row[2], '----', row[3], '----', row[4])

            else:
                print(row[0],"----", row[1], '----', row[2], '----', "***", '----', row[4])

        connection.commit()
        #close connection
        cursor.close()
        connection.close()

    def get_employee(empid):
        print("//==(Employee Information)==//")

        connection = connect_db()
        cursor = connection.cursor()

        sql = "select * from employees where id = %s"
        cursor.execute(sql, (empid,))
        rows = cursor.fetchall()

        for row in rows:
            # print(row)
            print("id-----  email--work_mood---salary--is_manager")
            if row[4] == 0:
                print(row[0],"----", row[1], '----', row[2], '----', row[3], '----', row[4])

            else:
                print(row[0],"----", row[1], '----', row[2], '----', "***", '----', row[4])

        connection.commit()
        #close connection
        cursor.close()
        connection.close()

    def hire(Employee):
        # print("emp name is " + str(Employee.email))
        connection = connect_db()
        cursor = connection.cursor()
        
        sql = "INSERT INTO `employees` (`id`, `email`, `work_mood`, `salary`, `is_manager`) VALUES (null, %s, %s, %s, %s)"
        val = (Employee.email, Employee.work_mood, Employee.salary, Employee.is_manager)
        cursor.execute(sql, val)
        connection.commit()

        print("Employee added successfully")
        #close connection
        cursor.close()
        connection.close()

    def fire(empid):
        print("=====(Delete Employee)=====")

        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("delete from employees where id= %s", (empid,) )
        connection.commit()
        print("employee deleted successfully")

        #close connection
        cursor.close()
        connection.close()

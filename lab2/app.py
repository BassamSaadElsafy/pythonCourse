from db_connect import*
from Person import Person
from Employee import Employee
from Office import Office
import re


def print_list():
    print("choose operation:")
    print("(1) Add new employee")
    print("(2) List all employees")
    print("(3) Get specific employee")
    print("(4) Delete specific employee")
    print("(5) Send E-mail")
    print("(6) Exit")

try:

    flag = True
    selected_option = -1

    while flag == True and selected_option != 6:
        
        print_list()
        selected_option = int(input("your choice: "))
        # if selected_option not in range(1,5):
        #     selected_option = int(input("*select number from above list: "))
        # else:
            
        if selected_option == 1:
            #regex for checking email 
            regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            email = input("enter employee email(ex@test.test): ")
            while not (re.search(regex, email)):
                print("Invalid Email")
                email = input("enter a valid email(ex@test.test): ")

            #salary
            salary = int(input("enter emp salary: "))
            while salary < 1000:
                salary = int(input("enter emp salary(1000 or more): "))

            #health rate
            health_rate = int(input("enter emp health rate: "))
            while health_rate not in range(1,100):
                health_rate = int(input("enter emp health rate(0 - 100): "))

            #is manager
            is_manager = int(input("enter emp level (1)manager (0)normal : "))
            while not (is_manager == 0)  and not (is_manager ==  1):
                is_manager = int(input("emp level must be (0 - 1): "))
            

            #  id, email, work_mood, salary, is_manager
            emp = Employee(email, 8, salary, is_manager)
            Office.hire(emp)

        elif selected_option == 2:
            Office.get_all_employees()

        elif selected_option == 3:
            emp_id = int(input("enter employee's id: "))
            Office.get_employee(emp_id)

        elif selected_option == 4:
            emp_id = int(input("enter employee's id: "))
            Office.fire(emp_id)

        elif selected_option == 5:
            to      = input("To: ")
            subject = input("Subject: ")
            body    = input("body: ")
            Employee.send_email(to, subject, body)

    else:
        print("Byebye")

except Exception as err:
    print("ERROR: " + str(err))


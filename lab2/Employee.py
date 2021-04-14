from Person import Person
import os

class Employee(Person):         #Employee inherits Person

    #initiate attributes for Person   
    def __init__(self, email, work_mood, salary, is_manager):
        self.id = id
        self.email = email
        self.work_mood = work_mood
        self.salary = salary
        self.is_manager = is_manager

    def work(hours):
        if   hours == 8 : 
            return "happy"
        elif hours > 8 :
            return "tired"

        else:
            return "lazy"

    def send_email(to, suject,bodyreceiver_name):

        path = "lab2/emails"

        #create folder if not exist
        if not os.path.exists(path):
            os.makedirs(path)

        #create file which represents the email
        filename = to + ".txt"
        file = open(os.path.join(path, filename) , "w+")
        file.write("To: " + to + "\n" + "Subject: " + suject + "\n" + "Body: " + bodyreceiver_name)
        file.close()
        print("mail sent successfully, file is generated")

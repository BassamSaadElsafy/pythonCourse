class Person:
    #attributes with initial values 
    full_name=""
    money=0
    sleep_mood=""
    health_rate=0

    def sleep(hours):
        if   hours == 7 : 
            return "happy"
        elif hours < 7 :
            return "tired"

        else:
            return "lazy"

    def eat(meals):

        if meals == 3 : 
            return 100               #health rate
        elif meals == 2 :
            return 75

        elif meals == 1:
            return 50

    def buy(items):

        if items == 1:
            self.money = self.money - 10

        
    
import random

#read games results from result file 
try:
    f_content = open("result_game", "r")
    content_list = f_content.read().split()

    print("wins  : " + content_list[1] + " times")
    print("loses : " + content_list[0] + " times")

except Exception as err:
    print("Welcome to our Game")

def check_number():

    win_count  = 0
    lose_count = 0

    #list of entered numbers
    entered_numbers = []

    random_number = random.randint(1, 100)
    level = 1

    print(random_number)
    i = 0

    while i < 10:

        try:
            num = int(input("enter your expected number, please: "))

            if num < 100 and num > 0:

                print(entered_numbers)

                if num in entered_numbers:
                    print("this number is entered before!")
                    continue

                entered_numbers.append(num)

                i = i + 1

                if num ==  random_number:
                    print("Congratulations")
                    random_number = random.randint(1, 100)
                    print("the rest tries are " + str(10 - i) + "\n level '" + str(level) + "' is Completed")
                    level = level + 1
                    win_count = win_count + 1
                    entered_numbers.clear()

                    print(random_number)
                elif num > random_number:
                    print("stimated number is less than entered value")
                else:
                    print("stimated number is greater than entered value")
            else:
                print("you should enter number between 1 and 100")

        except Exception as err:
            print(err)
    else:
        print("Game Over!")

        lose_count = lose_count + 1

        #read old results for updating 
        old_count_loses = 0 #intial value
        old_count_wins  = 0 #intial value
        try:
            file_content = open("result_game", "r")

            content_list = file_content.read().split()
            old_count_loses = content_list[0]
            old_count_wins  = content_list[1]

        except Exception as err:
            print("this was the first game you played" + str(err))

        print(old_count_loses)
        print(old_count_wins)

        file = open("result_game", "w")
        file.write(str(lose_count + int(old_count_loses)) + "\n" )
        file.write(str(win_count + int(old_count_wins)))
        file.close()

        play_again = input("Do you want to play again(y/n)? ")
        if( play_again.lower() == "yes" or play_again.lower() == "y"):
            check_number()
        else:
            print("Byebye :)")
    print("loses : ", lose_count)
    print("wins : ", win_count)

check_number()


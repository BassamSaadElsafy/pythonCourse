# a game generates a random number and give only 10 tries for the user to guess that number
import random

import os

if os.path.isfile("./log.txt"):
   
    file1 = open('log.txt', 'r')
    win_num  = int(file1.readline().split(':')[1])
    lose_num = int(file1.readline().split(':')[1])
    file1.close
    print("Welcome Back You Win: {} and Lose: {} ".format(win_num,lose_num))
else:
    logfile = open('log.txt', 'a')
    logfile.write("win:0\nlose:0")
    logfile.close()

trails = 10
in_list = []
i=0
randNum = random.randrange(100)
while i <= trails:
    
    in_number = int(input("Enter a number: "))
    if(in_number not in in_list):
        if(in_number == randNum):
            print("Congratulations")
            win_num+=1
            file_out = open("log.txt","a")
            file_out.write("Win:{}\nlose:{}".format(win_num,lose_num))
            file_out.close
            break
        elif((in_number < randNum) and (in_number < 100)):
            print("Hint: You less than the number")
            in_list.append(in_number)
            i+=1
        elif((in_number > randNum) and (in_number < 100)):
            print("Hint: You above the number")
            in_list.append(in_number)
            i+=1
        else:
            print("Out of range 100 ")
    else:
         print("Hint: you entered this number before")

print("Sorry you loss")
lose_num+=1
file_out = open("log.txt","a")
file_out.write("win:{}\nloss:{}".format(win_num,lose_num))
file_out.close
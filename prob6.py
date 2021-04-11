word = input("enter your string: ")
char = input("enter your char you want to search on the entered string: ")

res = []
for i in range(0, len(word)):
    
    if word[i] == char:
        res.append(i)
        
      
if not res:
    print ("charater '{}' not found in word '{}'".format(char, word))
else:
    print ("Character '{}' is present at {}".format(char, str(res)))


# print ("Occurrence of " + char + " is :\n "+ str(count))
# print ("Occurrence of all + " + word + " is :\n "+ str(freq)) 


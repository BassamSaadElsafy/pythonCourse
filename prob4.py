import sys
def most_frequent(list):
    word_counter = {}
    for word in list.split(" "):
        if len(word) > 0 and word != '\r\n':
            if word not in word_counter:
                word_counter[word]  = 1
            else:
                word_counter[word] += 1

    for i, word in enumerate(sorted(word_counter, key=word_counter.get,reverse=True)[:20]):
        print("{}: {} ({}) ".format(i+1,word,word_counter[word]))
        file1 = open("popular_words.txt","a")
        file1.write(word + " (" + str(word_counter[word]) + ")" +"\n")

    file1.close()

with open(sys.argv[1]) as f:
    contents = f.read()

most_frequent(contents)
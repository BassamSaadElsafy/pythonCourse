import sys
def most_common(list):
    common_words = []
    unique_words = []
    for word in list.split(" "):
        
        if word not in unique_words:
            unique_words.append(word)
            common_words.append( (list.split(" ").count(word), word ))

    sorted_words = sorted(common_words, reverse = True)

    for w in sorted_words[:20]:
        
        file1 = open("popular_words.txt","a")
        file1.write( str(w) + "\n")

with open(sys.argv[1]) as f:
    contents = f.read()

most_common(contents)
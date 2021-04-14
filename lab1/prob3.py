def splitter(s):
    mid = (len(s)+1)//2
    return s[:mid], s[mid:]

def front_back(a,b):
    a_front, a_back = splitter(a)
    b_front, b_back = splitter(b)
    return "".join((a_front, b_front, a_back, b_back))

print(front_back("Bassam", "Dev"))
def anti_vowel(c):
    
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            c = c.replace(x, "")        
    return c

str_word = input("enter a word, please: ")

print(anti_vowel(str_word))
def letters_replacement(s):
    s = s.replace('A', 'a')
    s = s.replace('B', 'A')
    s = s.replace('a', 'B')
    return(s)


s = "AABABBAABBBAB"
print(letters_replacement(s))


#
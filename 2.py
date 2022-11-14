import string 
def alphabet_position(text):
    return ' '.join([str(string.ascii_lowercase.index(i)+1) for i in ((''.join(filter(str.isalpha, text.lower())))) if i in string.ascii_lowercase])

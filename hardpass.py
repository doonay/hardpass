from string import ascii_letters
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import hexdigits
from string import octdigits
from string import punctuation
from string import printable
from string import whitespace

#print(ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#print(ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
#print(ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
#print(digits) # 0123456789
#print(hexdigits) # 0123456789abcdefABCDEF
#print(octdigits) # 01234567
#print(punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#print(printable) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#print(whitespace) # 
#Можно объединять несколько наборов в одну строку dict = digits + ascii_letters

from string import printable
from random import choice
import re

def check_symbols(password):
    flag = True
    lowercase = ascii_lowercase # abcdefghijklmnopqrstuvwxyz
    for char in lowercase:
        if char in password:
            print('Прописная есть...', end='')
        else:
            print('В пароле отсутствует прописная буква!')
            flag = False

    #any(char in ".,:;!_*-+()/#¤%&)" for char in password)

    # print(ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
    # print(ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # print(digits) # 0123456789
    # print(punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    return True

def get_cool_password():
    dict = punctuation.replace('+', '!') + ascii_letters
    pass_length = 15
    password = ''.join(choice(dict) for _ in range(pass_length))
    #print(check_symbols(password))
    #return password if (password.find(ascii_uppercase) != -1 and password.find(ascii_lowercase) != -1 and password.find(punctuation) != -1) else get_cool_password()
    return password

if __name__ == ('__main__'):
    #print(get_cool_password())
    pass
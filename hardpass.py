#from string import ascii_lowercase
#from string import ascii_uppercase
#from string import hexdigits
#from string import octdigits
#from string import punctuation
#from string import printable
#from string import whitespace

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

#from string import printable

from string import digits
from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation
from string import ascii_letters
from random import choice
import re

def check_symbols(password):
    lowercase_flag = False
    uppercase_flag = False
    special_symbols_flag = False
    digits_flag = False

    lowercase = ascii_lowercase# abcdefghijklmnopqrstuvwxyz
    uppercase = ascii_uppercase# abcdefghijklmnopqrstuvwxyz
    special_symbols = '\'\#!"$%&()*,-./:;<=>?@[\]^_`{|}~'
    #digits = digits

    for char in password:
        if char in lowercase: #проверка на нижний регистр
            print(char, 'есть ловеркейс')
            lowercase_flag = True
            continue
        else:
            #print(char, 'не ловеркейс')
            pass

        if  char in uppercase: #проверка на верхний регистр
            print(char, 'есть апперкейс')
            uppercase_flag = True
            continue
        else:
            #print(char, 'не апперкейс')
            pass

        if char in special_symbols: #проверка на спецсимвол
            print(char, 'есть спецсимвол')
            special_symbols_flag = True
            continue
        else:
            #print(char, 'не спецсимвол')
            pass

        if char in digits: #проверка на цифру
            print(char, 'есть цифра')
            digits_flag = True
            continue
        else:
            #print(char, 'не цифра')
            pass

        print('--------')
        if lowercase_flag + uppercase_flag + special_symbols_flag + digits_flag:
            break
        else:
            continue

    return True if lowercase_flag + uppercase_flag + special_symbols_flag + digits_flag else False

def get_cool_password():
    new_punctuation = punctuation.replace('+', '!') + ascii_letters + digits# проверка на плюс, плюс нельзя!

    pass_length = 15

    while True:
        password = ''.join(choice(new_punctuation) for _ in range(pass_length))
        print(password)
        if check_symbols(password):
            return password

if __name__ == ('__main__'):
    print(get_cool_password())

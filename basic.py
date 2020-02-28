# basic
# 
# Author: Paal Pedersen
# Email: paalped@gmail.com
# Description:
# This script contains a simple algorithm for encrypting and decrypting
# a secret string with with a key



from random import seed, randint

__all__ = ['encrypt', 'decrypt']

def _fill_letters(lower_char_index: int, upper_char_index: int):
    # a function for creating random letters in a string
    # it accepts a range for character creation function chr
    letters = []
    n = upper_char_index - lower_char_index
    while len(letters) < n:
        char = chr(randint(lower_char_index, upper_char_index))
        if char not in letters:
            letters.append(char)
    return ''.join(letters)

def encrypt(key: str, secret: str, gap: tuple = (32,288)):
    low, high = gap
    n = high - low
    width = len(str(n))
    key = '1' + ''.join(map(lambda x: '{0:0>{1}}'.format(ord(x), width), key))
    seed(int(key)) # Crusial for getting the same pseudo random numbers
    left = _fill_letters(*gap)
    right = _fill_letters(*gap)
    transtable = str.maketrans(left, right)
    return secret.translate(transtable)

def decrypt(key: str, encrypted_secret: str, gap: tuple = (32,288)):
    low, high = gap
    n = high - low
    width = len(str(n))
    key = '1' + ''.join(map(lambda x: '{0:0>{1}}'.format(ord(x), width), key))
    seed(int(key)) # Crusial for getting the same pseudo random numbers
    left = _fill_letters(*gap)
    right = _fill_letters(*gap)
    transtable = str.maketrans(right, left)
    return encrypted_secret.translate(transtable)

if __name__ == '__main__':
    c = encrypt('ytu', 'My super secret word', gap=(0,1000))
    print(c)
    print()
    print(decrypt('ytu', c, gap=(0,1000)))

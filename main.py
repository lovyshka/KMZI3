import math
import random


with open('open_text', 'r') as f:
    text = f.read()

p = 48374365282328868173
q = 47569106160836889337

def resheto_erastofena(n:int):
    a = []
    sieve = set(range(2, n + 1))
    while sieve:
        prime = min(sieve)
        sieve -= set(range(prime, n + 1, prime))
        a.append(prime)
    return a



def power_mod(x: int, pow: int, mod: int):
    res = 1
    pow_res = 0
    while pow_res < pow:
        pow_res_1 = 2
        res1 = x
        while pow_res + pow_res_1 <= pow:
            res1 = (res1 * res1) % mod
            pow_res_1 *= 2
        pow_res_1 //= 2
        res = (res * res1) % mod
        pow_res += pow_res_1
    return res % mod

def clear_nulls(out_str):
    while out_str[0:8] == '00000000':
        out_str = out_str[8:]
    return out_str

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def gen_keys():
    n = p * q
    eiler_func = ((p - 1) * (q - 1))
    arr_of_e = []
    # for e in range(2, eiler_func):
    #     if (gcd(eiler_func, e) == 1):
    #         arr_of_e.append(e)
    # # e = random.choice(arr_of_e)
    e = int(input('Введите значение е'))

    return e, n

def encrypt(text):
    e, n = gen_keys()
    block_len = int(math.floor(math.log2(n)))
    if len(text) % block_len != 0:
        text = '0' * (block_len - (len(text) % block_len)) + text
    start_arr = [text[i:i + block_len] for i in range(0, len(text), block_len)]
    message_str = ''
    for i in start_arr:
        c = bin(power_mod(int(i,2), e, n))[2:]
        if len(c) < block_len + 1:
            dop = '0' * (block_len + 1 - len(c))
            c = dop + c
        message_str += c

    return message_str

def decrypt(message_str):
    e, n = gen_keys()
    d = mulinv(e, ((p - 1) * (q - 1)))
    block_len = int(math.floor(math.log2(n))) + 1
    if len(message_str) % block_len != 0:
        message_str = '0' * (block_len - (len(message_str) % block_len)) + message_str
    start_arr = [message_str[i:i + block_len] for i in range(0, len(message_str), block_len)]
    out_str = ''
    for i in start_arr:
        ci = bin(power_mod(int(i, 2), d, n))[2:]
        if len(ci) < block_len - 1:
            dop = '0' * (block_len - 1 - len(ci))
            ci = dop + ci

        out_str += ci
    out_str = clear_nulls(out_str)
    if len(out_str) % 8 != 0:
        out_str = out_str[(len(out_str) % 8):]
    return out_str

print(decrypt('100110011001001011100011110000010111011111110101001001000110010011001001100011101111100100011100011001111000010100010100000010010100110000111011000000011101100110011000011011010011100010100010111011001100011000011100101101100001100001100001011101111010010000110100111111011101100110011000011011010011100010100010111000111011010101000100001110111000011010110011001111111011010000111011010101000001011110110010011110001011100010011110000000111001011101011101010011111011011010001011000101001101111001100001101000010011000101101000100111010010100001100100101010001101000011'))



# vibor = input('Сгенерировать? (1 - да/0 - нет)' + '\n')
#
#
#
# if vibor == '1':
#     print(resheto_erastofena(int(input('Введите число, до которого сгенерировать простые числа:'))))
#     print('Происходит генерация простых чисел')

#print(start_arr)





# c = (m ** e) % (p * q)




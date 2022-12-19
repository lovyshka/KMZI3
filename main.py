import math
from math import gcd
#import random


with open('open_text', 'r') as f:
    text = f.read()

p = 4402586860135658839858157070373844599860222172231172492190567678379130634509062126747060384354581289
q = 3864665030946857310880421239030529638898978886946796468645568121762676596278903074413914637196474807

def resheto_erastofena(n:int):
    a = []
    sieve = set(range(2, n + 1))
    while sieve:
        prime = min(sieve)
        sieve -= set(range(prime, n + 1, prime))
        a.append(prime)
    return a

# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = extended_gcd(b % a, a)
#         return gcd, y - (b // a) * x, x


def power_mod(x:int, pow:int, mod:int):
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
    e = 5

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
    print(len(out_str), out_str)
    # if len(out_str) % 8 != 0:
    #     out_str = out_str[len(out_str) -(len(out_str) // 8 * 8):]
    return out_str

print(decrypt('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001011100011000110100111001101010111110101110011111001101101011010111010011100000101111101000000110101111001010011001010100100111011001111110000001000010101'))




# vibor = input('Сгенерировать? (1 - да/0 - нет)' + '\n')
#
#
#
# if vibor == '1':
#     print(resheto_erastofena(int(input('Введите число, до которого сгенерировать простые числа:'))))
#     print('Происходит генерация простых чисел')

#print(start_arr)





# c = (m ** e) % (p * q)




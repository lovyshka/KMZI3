
# x = '010000110101001001011001010100000101010001001111'
# if len(x) % 7 != 0:
#     x += '0' * (7 - len(x) % 7)
#
# start_arr = [x[i:i + 7] for i in range(0, len(x), 7)]
#
#
# print(start_arr)
# for i in start_arr:
#     print(len(i))
#
# print(len('010000110101001001011001010100000101010001001111'))


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

# def power_mod(x:int, pow:int, mod:int):
#     assert type(x) is int
#     assert type(pow) is int and pow >= 0
#     assert type(mod) is int
#     res = 1
#     pow_res = 0
#     while pow_res < pow:
#         pow_res_1 = 2
#         res1 = x
#         while pow_res + pow_res_1 <= pow:
#             res1 = (res1 * res1) % mod
#             pow_res_1 *= 2
#         pow_res_1 //= 2
#         res = (res * res1) % mod
#         pow_res += pow_res_1
#     return res % mod
#
# print(power_mod(1234567890, 1234567890, 247))
# print((1234567890 ** 1234567890) % 247)
#
# def gcd_extended(num1, num2):
#     if num1 == 0:
#         return (num2, 0, 1)
#     else:
#         div, x, y = gcd_extended(num2 % num1, num1)
#     return (div, y - (num2 // num1) * x, x)

#
# def resheto_erastofena(n:int):
#     a = []
#     sieve = set(range(2, n + 1))
#     while sieve:
#         prime = min(sieve)
#         sieve -= set(range(prime, n + 1, prime))
#         a.append(prime)
#     return a

#
# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = extended_gcd(b % a, a)
#         return gcd, y - (b // a) * x, x


# print(extended_gcd(5, 216) % 216)
import time

def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.2f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time



@timeit
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

@timeit
def prosto():
    return ((123 ** 12312312) % 25)

# print(power_mod())
# print(cProfile.run('prosto()'))
# print((123123456789 ** 123123456789) % 25)
# print(power_mod(123123456789, 123123456789, 25))
# print(len('00000000000000000000'))
print(read())
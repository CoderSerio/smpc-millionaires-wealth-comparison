import math
import random

# 这里就朴素地筛一下, 高级的筛法忘了...


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# 求最大公约数


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 求解 (e * d) % s == 1 中的 d


def find_priv_key(e, s):
    for d in range(100000000):
        if (e * d) % s == 1:
            return d
    return -1

# 获取小于指定的数的所有素数


def get_prime_arr(max):
    prime_arr = []
    for i in range(2, max):
        if is_prime(i):
            prime_arr.append(i)
    return prime_arr


#  找出指定范围内，与 n 互质的整数 e
def find_pub_key(n, max):
    # 保证获取的随机性
    while True:
        e = random.randint(1, max)
        if gcd(e, n) == 1:
            break
    return e


def build_key():
    prime_arr = get_prime_arr(1000)
    p = random.choice(prime_arr)
    # 保证p和q不为同一个数
    while True:
        q = random.choice(prime_arr)
        if q != p:
            break
    n = p * q
    s = (p - 1) * (q - 1)
    e = find_pub_key(s, 1000)
    d = find_priv_key(e, s)

    return n, e, d


# 加密
def rsa_encrypt(A, ned):
    '''
    密文B = 明文A ^ e % n, ned为公钥
    '''
    B = pow(A, ned[1]) % ned[0]
    return B


# 解密
def rsa_decrypt(B, ned):
    '''
    明文A = 密文B ^ d % n, ned为私钥
    '''
    A = pow(B, ned[1]) % ned[0]
    return A

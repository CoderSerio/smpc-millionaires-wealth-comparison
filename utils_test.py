from utils import build_key, rsa_decrypt, rsa_encrypt
import random

public_and_private_key = build_key()

public_key = (public_and_private_key[0], public_and_private_key[1])  # 公钥
private_key = (public_and_private_key[0], public_and_private_key[2])  # 私钥

test_n = random.randint(0, 100)
test_e = rsa_encrypt(test_n, public_key)
test_d = rsa_decrypt(test_e, private_key)

print('原数字n={}\n加密后的数字e={}\n解密后的数字d={}'.format(test_n, test_e, test_d))

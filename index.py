from utils import build_key, rsa_encrypt, rsa_decrypt
import random

# 两位富翁
person_a = random.randint(1, 9)
person_b = random.randint(1, 9)
print(f"两位富翁的金钱, a={person_a}, b={person_b}")

keys = build_key()
public_key = (keys[0], keys[1])
private_key = (keys[0], keys[2])

# 生成一个随机大数，用公钥加密后发送给b
random_big_num = random.randint(1, 1000)
encrypt_num = rsa_encrypt(random_big_num, public_key)
num_a_2_b = encrypt_num - person_a
print(f"【A】随机选取的大整数{random_big_num}，加密后:{encrypt_num}, 发送给B的密文: {num_a_2_b}")

# 收到之后尝试解密
decrypted_num_list = []
for i in range(1, 11):
    # 对 num_a_2_b + i 进行解密
    decrypted_num = rsa_decrypt(num_a_2_b + i, private_key)
    decrypted_num_list.append(decrypted_num)

print(f"【B】收到数据后，尝试解密之后的10个结果:\n{decrypted_num_list}")

# 选取合适大小的模数，这里选100以内的
num_list_b_2_a = []
random_mod_num = 0

while True:
    # 每次选取都要重置一下num_list_b_2_a
    num_list_b_2_a = []
    random_mod_num = random.randint(1, 100)
    for i in range(0, 10):
        processed_num = decrypted_num_list[i] % random_mod_num
        if processed_num <= 100:
            num_list_b_2_a.append(processed_num)
        else:
            break
    if len(num_list_b_2_a) >= 10:
        break

print(f"【B】随机选取的模数:{random_mod_num}，对解密结果取模得到10个数:\n{num_list_b_2_a}")

# 前person_b位不变
for i in range(person_b, 10):
    num_list_b_2_a[i] += 1

print(f"【B】对[{person_b}(富翁a的财富值), 10)这个区间进行+1操作，得到要发送给B的10个数:\n{num_list_b_2_a}")


# 最后，A验证一下数字(从0开始计数所以-1)
person_a_num = num_list_b_2_a[person_a - 1]
test_num = random_big_num % random_mod_num

print(
    f"【B】person_b={person_a}, person_b_num={person_a_num}, test_num={test_num}, num_list_a_2_b={num_list_b_2_a}")

if person_a_num == test_num:
    print(f"【B】财富: A<B")
else:
    print(f"【B】财富: A>=B")

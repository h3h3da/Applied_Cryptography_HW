from gmssl import sm3, func
from struct import pack
from my_sm3 import sm3_hash

def create_hash(secret, message):
    return sm3.sm3_hash(func.bytes_to_list(bytes(secret + message, encoding='utf-8')))

def check_hash(pre_hash, my_hash):
    if pre_hash == my_hash:
        print("SM3 Hash长度扩展攻击成功！")
    else:
        print("SM3 Hash长度扩展攻击失败！")

def create_mysm3hash(data, new_iv):
    return sm3_hash(data, new_iv)

def getpadding(secret_len, message):
    padding=func.bytes_to_list(bytes(message, encoding='utf-8'))
    padding.append(0x80)
    data_len = len(message) + secret_len
    for i in range(64-8-1-data_len):
        padding.append(0x00)
    padding.extend(func.bytes_to_list(pack(">Q", (secret_len+ len(message))*8))) # ！！！！ 注意这里要大端序标识secret + message的总的bit位数
    # padding = "{zero}".format(zero = "\x00" * (64 - data_len - 1 - 8))
    # print(type(pack(">Q", (secret_len+ len(message))*8)))
    # padding = str('\x80') + padding + str(pack(">Q", secret_len+ len(message)))
    return padding

def get_new_iv(IV):
    # 替换新的IV
    new_iv = []
    for i in range(8):
        iv_seg = IV[i * 8:i * 8 + 8]
        new_iv.append(int(iv_seg, 16))
        # print(type(iv_seg))
    # print(new_iv)
    return new_iv

secret='sspku' #len(secret) = 5
message='hello,world'

IV = create_hash(secret, message)

append = 'attack'
print("secret: " + secret)
print("Input message: " + message + "\nInput append message: " + append)
padding = getpadding(len(secret), message)
print("padding: " + str(padding))
new_iv = get_new_iv(IV)
print("NEW_IV = sm3(sercret + massage) = " + str(IV))
fake_data = func.bytes_to_list(bytes("beida", encoding='utf-8')) # 已知secret长度为五位，这里随便用五位字符填充即可
fake_data.extend(padding)
fake_data.extend(func.bytes_to_list(bytes(append, encoding='utf-8')))
new_data=func.bytes_to_list(bytes(secret, encoding='utf-8'))
new_data.extend(padding)
new_data.extend(func.bytes_to_list(bytes(append, encoding='utf-8')))

# print("input data", fake_data)
print("sm3_hash(secret + message + padding + append) = " + str(sm3.sm3_hash(new_data)))
print("my_hash(message + padding + append) = " + str(create_mysm3hash(fake_data, new_iv)))
check_hash(sm3.sm3_hash(new_data), create_mysm3hash(fake_data, new_iv))

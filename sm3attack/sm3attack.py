from sm3 import sm3hash
from gmssl import sm3, func
from struct import pack

def create_hash(secret, message):
    return sm3.sm3_hash(func.bytes_to_list(bytes(secret+message, encoding='utf-8')))

def create_mysm3(data):
    return sm3hash(data)

def create_mysm3hash(data, IV):
    return sm3hash(data, IV)

def check_hash ( secret, message, my_hash ):
    pre_hash = create_hash(secret, message)
    print("pre_hash: " + pre_hash)
    print("my_hash: " + my_hash)
    if my_hash == pre_hash:
        print("Attack successful!")
    else:
        print("Attack failed!")
    return # my_hash == pre_hash

def getpadding(secret_len, message, m):
    data_len = len(message) + secret_len
    padding = message + "\x80{zero}".format(zero = "\x00" * (64 - data_len - 1 - 8))
    padding = bytes(padding, encoding = 'utf-8') + pack(">Q", secret_len+ len(message)) + bytes(m, encoding = 'utf-8')
    return padding

secret='sspku' #len(secret) = 5
message='hello,world'

IV = create_hash(secret, message)
m = 'attack'
print("secret: " + secret)
print("Input message: " + message + "\nInput append message: " + m)
padding = str(getpadding(len(secret), message, m))
print("padding: " + padding)

check_hash(secret, padding, create_mysm3hash(m, IV))


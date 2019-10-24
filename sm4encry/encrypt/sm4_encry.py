import os
import hashlib
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT

my_md5 = hashlib.md5()
my_md5.update("pku".encode('utf-8'))
key = bytes(my_md5.hexdigest(), encoding='utf-8')
my_md5.update("sspku".encode('utf-8'))
iv = bytes(my_md5.hexdigest(), encoding='utf-8')

def sm4ecb(outfile):
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key, SM4_ENCRYPT)
    with open("./pku_logo.rgb", 'rb') as f:
        logo_data = f.read()
        encrypt_logo = crypt_sm4.crypt_ecb(logo_data)
        f.close()
    with open(outfile, 'wb') as f:
        f.write(encrypt_logo)
        f.close()

def sm4cbc(outfile):
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key, SM4_ENCRYPT)
    with open("./pku_logo.rgb", 'rb') as f:
        logo_data = f.read()
        encrypt_logo = crypt_sm4.crypt_cbc(iv, logo_data)
        f.close()
    with open(outfile, 'wb') as f:
        f.write(encrypt_logo)
        f.close()

def main():
    os.system('magick convert pku_logo.png pku_logo.rgb')
    sm4ecb('sm4ecb.rgb')
    os.system("magick -size 432x465 -depth 8 sm4ecb.rgb sm4ecb.png") # 这里的大小需要根据pku_logo.png的大小来设置
    sm4cbc('sm4cbc.rgb')
    os.system("magick -size 432x465 -depth 8 sm4cbc.rgb sm4cbc.png") # 这里的大小需要根据pku_logo.png的大小来设置


if __name__ == '__main__':
    main()
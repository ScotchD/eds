from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

#Передаем файл
fname = "ot.docx"
with open(fname, "r", encoding='utf-8') as f:
    print("Содержимое файла:", f.read())

#Передаем открытый ключ
pubkey_export = b'-----BEGIN PUBLIC KEY-----' \
                b'\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCux4XSFojehKdKLBOxqnZezBIW' \
                b'\nU9mGvrIwsnOhbCw/3R7yjNRozzs3J95OoB867l94NNGRK/Zm59F0CqNCjVpUelFJ' \
                b'\nDjCbEQmg5XAwplG0ij0xpQBk6Ws3ySSdSQ36h8YJLbYmWeShxdwCWDynklPGJKDl' \
                b'\nccFHBlZo6sKqr7v7ZQIDAQAB' \
                b'\n-----END PUBLIC KEY-----'
pubkey = RSA.import_key(pubkey_export)

#Передаем подпись
signature = b'o\xb8z2F\x94\x8bN\xd1_\xb8\x9d\n\x10RO\x1e\xd9\xea\xebb\xb7\x0b\xe7\xa4\x076\xb7=\xc1C\xe8\x8d\xaf\x14_\xdb<\xfa\xbf\xb4{\xff9\xd0\xee\xfc<7\xe9_%\x93\xaa\t\xfa\x81\xe8\xf1\xea\xb5c\xcb\xec\xc3\x8f\x8a\xe5\xcf\xf4\xa9\x14$\'I \x03U\x8e)\x92\xe2\x91\xb1\xba09A\x85_\xe0s2\x9f\x90\x05\xf8\xf8\xd1\xd6@o\x02\x9bh.\xff\x9d"\xe1\xcar\x9d\xde\x04\xa3\x91\x10V\x86\xb65\x8a\x8c3\xac\xc1\xf2'

#Считаем хеш
h = SHA256.new()
with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        h.update(chunk)
print("Новый хэш:", h.hexdigest())

#Проверяем
try:
    pkcs1_15.new(pubkey).verify(h, signature)
    print("Проверка подписи прошла успешно")
except ValueError:
    print("Подпись не прошла проверку")

#0d07e7675100391173efac1f6b13980f7cf75210d35e89ed5400756b72b62aaa
#0d07e7675100391173efac1f6b13980f7cf75210d35e89ed5400756b72b62aaa
#3cb4bb04dd3e1c71e814507675f7a5bd853c27672e5d21c66a617152943320d2
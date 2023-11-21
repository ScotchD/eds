from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import os

fname = "ot.docx"
with open(fname, "r", encoding="utf-8") as f:
    print("Содержимое файла:", f.read())

# Генерация нового ключа
#key = RSA.generate(1024, os.urandom)
#key_export = key.exportKey
#print("Закрытый ключ:", key_export)

# Создание закрытого ключа
key_export = b'-----BEGIN RSA PRIVATE KEY-----' \
             b'\nMIICXAIBAAKBgQCux4XSFojehKdKLBOxqnZezBIWU9mGvrIwsnOhbCw/3R7yjNRo' \
             b'\nzzs3J95OoB867l94NNGRK/Zm59F0CqNCjVpUelFJDjCbEQmg5XAwplG0ij0xpQBk' \
             b'\n6Ws3ySSdSQ36h8YJLbYmWeShxdwCWDynklPGJKDlccFHBlZo6sKqr7v7ZQIDAQAB' \
             b'\nAoGAB9/n9Nr8kDAAXIxnV8AjJKrDnttox9QkMaL8qDd4N+llyU5UjKNXmujSMI8w' \
             b'\n0QYn6YHRtl15dNH5gyWujONTADuwE1Cc9Dlf25JJTJK9uX4U+EIaK4TeVrW+EzJj' \
             b'\nIme+aUrebntE+BNb4WM1zLvdwJJPiS66aTDd4DJNA6DAuUkCQQC8AKJ4sd6l4XJv' \
             b'\nPyD+j6AXEHol9hVwi7nmoz8oNseKLHfxaPqCS/jPtTtvUhiUeHrTHyfu6Tj8Uc+q' \
             b'\nXnPUmfupAkEA7f6L83mXb0osEKKa/5+NsX4kDwKKVluHgFZp5qMRXK5ZqLLs4aLR' \
             b'\nNGexbB5jPNgzO3nZ7Olx6e8BUXPvQ1B3XQJAI8TnJJmK5/ql4B6ds3E2H01GQDS6' \
             b'\nzYf4HbaPjKIngtWFGIxFpUa5FyO/JCX1gUIO9F4oJd9/tRoHrb18wkVtyQJBANSt' \
             b'\n8tcjw8Z6XCKJjUX+iZsiBIs9U+6UYOS5VG39L5jJXeo56yJAZAAW4iCij0BiXHY8' \
             b'\nEBl9DIVnRqBJoHlhQSkCQGJCzSq8opG66MbVX4Xs0OXlh5/ZWTDNnoBUiiPQWoN6' \
             b'\ndu7kP6QLXN0NpMfwpmjBHmJnitVRIj91ZLOzvRc3T+g=' \
             b'\n-----END RSA PRIVATE KEY-----'
key = RSA.importKey(key_export)
print("Закрытый ключ:", key_export)

# Получение открытого ключа из закрытого
pubkey = key.publickey()
print("Открытый ключ:", pubkey.exportKey())

# Получение хэш файла
h = SHA256.new()
with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        h.update(chunk)
print("Новый хэш:", h.hexdigest())

# Подписание хэш
signature = pkcs1_15.new(key).sign(h)
print("Подписание хэша с помощью ключа:", signature.hex())
print(signature)

with open("подпись.txt", "a") as f:
    f.write(signature.hex(" ") + '\n')
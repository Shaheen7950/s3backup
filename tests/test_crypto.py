from s3backup.crypto import encrypt, decrypt

result = encrypt(b"my secret backup data", "correct horse battery staple")
print(decrypt(result, "correct horse battery staple"))
print(decrypt(result, "wrong passphrase"))

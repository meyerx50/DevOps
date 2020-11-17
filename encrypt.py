import hashlib
password = "This is my password"
print(hashlib.md5(password.encode('utf-8')).hexdigest())
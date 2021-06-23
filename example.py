import crypto
hash=crypto.encrypt('sibinmdkm@gmail.com','Thomas')
#crypto.encrypt('text',password)
print(hash)
print(crypto.decrypt(hash,'Thomas'))
#crypto.decrypt(cypher,password)

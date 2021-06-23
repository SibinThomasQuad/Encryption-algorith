import crypto
hash=crypto.encrypt('hai ruby this is the message that what im sending on the computer is why','locationspoofedbysame')
#crypto.encrypt('text',password)
print(hash)
print(crypto.decrypt(hash,'locationspoofedbysame'))
#crypto.decrypt(cypher,password)

def password_sum(password):
    pass_code=0
    for word in password:
        asci=ord(word)
        pass_code=pass_code+asci
        return pass_code
def password_length(password):
    length=len(password)
    return length
def decrypt(cypher,password):
    skelt=''
    cypher=int(cypher, 16)
    pass_code=password_sum(password)
    pass_length=password_length(password)
    salt=pass_code*pass_length**2
    string_list = str(cypher).split(str(salt))
    while("" in string_list):
        string_list.remove("")
    #print(string_list)
    for numbers in string_list:
        decoded=chr(int(numbers) // int(pass_length) // int(pass_code) // int(salt))
        skelt=skelt+str(decoded)
    return skelt
def encrypt(string,password):
    #line
    skelt=''
    pass_code=password_sum(password)
    pass_length=password_length(password)
    salt=pass_code*pass_length**2
    for word in string:
        #line
        asci=ord(word)*salt*pass_code*pass_length
        skelt=skelt+str(asci)+str(salt)
    return hex(int(skelt))

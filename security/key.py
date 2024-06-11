from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# print(key)
# with open('secret.key', 'wb') as key_file:
#     key_file.write(key)
# print("Key generated and stored successfully.")
def security(password):
    fileopen = open("secret.key","r")
    key = fileopen.read()
    fileopen.close()
    # print(key)
    temp = Fernet(key)
    name = password
    # token = temp.encrypt(b"rishabh13454")
    token = temp.encrypt(name.encode())
    print(token)
    with open('rishabh.key', 'wb') as key_file:
        key_file.write(token) 
    encrypted_bytes = b'gAAAAABmXdtzfxs-SGAE_pzeWO6dxLIu6_ab-LWnggKApKWH3lJowm_bJlUqnwHlyjSDV-bwtfG6l8WdZf56xex5lbEJ7YyPyA=='

    # # Convert by    tes to string
    encrypted_string = encrypted_bytes.decode('utf-8')
    print(encrypted_string)
    print(str(encrypted_bytes) == str(token))
    print("token "+str(token))
    return temp.decrypt(token).decode()
    return str(token)

    # print("encrypted key: "+str(token))

    # new_text = temp.decrypt(token).decode()
    # print(new_text) 

security("hello diana")
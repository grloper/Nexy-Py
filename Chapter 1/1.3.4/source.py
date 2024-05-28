password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
decoded_password = "".join([chr(ord(char) - 2) if char.isalpha() else char for char in password])
print(decoded_password)

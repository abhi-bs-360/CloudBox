# Fixed XOR

from binascii import unhexlify

def xor_string(x, y):
    z = [chr(ord(i) ^ ord(j)) for i, j in zip(x, y)]
    return "".join(z)

hex_string = "1c0111001f010100061a024b53535009181c"
key_string = "686974207468652062756c6c277320657965"

decoded_hex_string = unhexlify(hex_string).decode()
decoded_key_string = unhexlify(key_string).decode()

print(decoded_hex_string, decoded_key_string)
print('\n')

result = xor_string(decoded_hex_string, decoded_key_string)
print(result)

encoded_result = result.encode()
print(encoded_result)
print(type(encoded_result))
print(encoded_result.hex())
print('\n')

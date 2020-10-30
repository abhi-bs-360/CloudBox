# Single_byte_XOR cipher

from binascii import unhexlify

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
decoded_hex_string = unhexlify(hex_string).decode()

for i in range(65, 91):
    result = ""
    for j in decoded_hex_string:
        result += chr(ord(j) ^ i)
    print('\n', chr(i), '  ', result)

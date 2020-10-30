# Converting hex to base_64

import codecs as c
from binascii import unhexlify, b2a_base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

result0 = c.encode(c.decode(hex_string,'hex'), 'base64').decode()

result1 = b2a_base64(unhexlify(hex_string)).decode()

result2 = b2a_base64(bytes.fromhex(hex_string)).decode()

# All the three below gives same result
print(result0)
print(result1)
print(result2)

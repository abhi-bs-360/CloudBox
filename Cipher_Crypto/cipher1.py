message = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
result = []
n = len(message)
c = 0
print('\n')

for i in range(n):
    if c == 0:
        result += chr(ord(message[i]) ^ ord('I'))
        c += 1
    elif c == 1:
        result += chr(ord(message[i]) ^ ord('C'))
        c += 1
    elif c == 2:
        result += chr(ord(message[i]) ^ ord('E'))
        c = 0

x = "".join(result)
x = x.encode()
print(x.hex(), '\n')

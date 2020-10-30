def isPrime(num):
    if 1 < num < 4:
        return True
    if num < 2:
        return False
    if num%2 == 0 or num%3 == 0:
        return False
    for i in range(5, int(num**0.5)+1, 6):
        if num%i == 0 or num%(i+2) == 0:
            return False
    return True

def generate(N):
    i, pcount, result = 2, 0, []
    while pcount != N:
        if isPrime(i):
            result.append(i)
            pcount += 1
        i += 1
    return result

word1 = input("Enter a word : ")
word2 = input("Enter another word : ")
alpha = [chr(x) for x in range(97,123)]
primes =  generate(26)
box = dict(zip(alpha, primes))
xor1, xor2 = 1, 1
for letter in word1:
    xor1 ^= box[letter]
for letter in word2:
    xor2 ^= box[letter]
print(xor1, " ", xor2)
if xor2 == xor1:
    print("AnAgRaM")
else:
    print("Not an aNaGrAm")

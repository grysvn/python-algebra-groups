'''
Here are the steps of the El Gamal encryption algorithm. Note, this algorithm is not intended for realistic security purposes as presented.

Bob does the following once.
(a) Chooses a group G
(b) Choose g ∈ G
(c) Choose a natural number k
(d) Compute h = g^k
(e) Tell the whole world: G, g, h.
Alice does the following whenever she wants to send a message to Bob.
(a) Encode the message as m ∈ G using an international standard.
(b) Choose a natural number s.
(c) Encrypt m into c1 = g^s and c2 = h^s * m.
(d) Sends to Bob (using insecure channel): c1, c2.
Bob does the following upon receiving series of c1, c2 from Alice.
(a) Decrypt c1 and c2 into m0 = c^(−k) * c2.
(b) Decode m0 using the international standard.
'''

#import parent dir
#https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import os,sys,inspect
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from groups import *

def power(G,e,n):
    '''
    G:  group
    e:  element
    n:  exponent
    '''
    result = G.identity()
    for i in range(0,n):
        result = G.compose(result, e)
    return result

def initialization(G, g, k):
    '''
    G:  group to use for encryption
    g:  element of group to use
    k:  natural number
    '''

    h = power(G, g, k)
    return (G, g, h)

def encrypt(init, msg, encode, s):
    '''
    init:   results from initialization
    msg:    string msg to encode 
    encode: function taking one param (msg) 
    s:      natural number
    '''

    G = init[0]
    g = init[1]
    h = init[2]

    m = encode(msg)
    c1 = power(G, g, s)
    c2 = G.compose(power(G, h, s), m)
    return (c1, c2)

def decrypt(G, c1, c2, k):
    '''
    G:  group
    c1: part 1 of encrypted data
    c2: part 2 of encrypted data
    k:  private key
    '''

    return G.compose(power(G, G.inverse(c1), k), c2)

G = U(7)
k = 9
g = 3
init = initialization(G, g, k)
msg = 2 #"secret" message
encode = lambda x: x
s = 5
encrypted_data = encrypt(init, msg, encode, s)
decrypted = decrypt(G, encrypted_data[0], encrypted_data[1], k)

print("The original message is {0}".format(msg))
print("Part 1 (c1) of the encrypted data is {0}".format(encrypted_data[0]))
print("Part 2 (c2) of the encrypted data is {0}".format(encrypted_data[1]))
print("The decrypted message is (should equal the original) {0}".format(decrypted))


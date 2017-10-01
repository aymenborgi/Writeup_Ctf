#This is a quick and dirty writeup for Working Junks
from binascii import *
file = open('enc','r') #The binary gives us 4 parts, we are interested only in the last part which is our flag
a = file.read()

def encryptdecrypt(a):
	s = []
	for i in range(len(a)):
		s.append(chr(ord(a[i])^0x4B))
	return s
def encryptdecrypta(s):
	v = []
	for j in range(len(s)):
		v.append(chr(ord(s[j])^0x58))
	return v
def encryptdecryptb(v):
	k = []
	for f in range(len(v)):
		k.append(ord(v[f])^0x6f)
	return k

c = []
d = []
l = []
c = encryptdecrypt(a)
d = encryptdecrypta(c)
l = encryptdecryptb(d)


print (''.join(str(hex(v).split('x')[-1]) for v in l)).decode('hex') # python solve.py |xxd -r p > flag






from Crypto.Cipher import AES
import base64
import os
import pyminizip
import uuid
import bcrypt
BLOCK_SIZE = 32
PADDING = '{'
secret = os.urandom(BLOCK_SIZE)
SECRET = base64.b64encode(secret)


def info():
    a = "AES-192"
    return a

def keychain(key, store):
    compression_level = 5
    p = str(uuid.uuid4())
    h = bcrypt.hashpw(p, bcrypt.gensalt())
    pyminizip.compress("{}.h5k".format(key), "{}.h5ks".format(store), h, compression_level)
    print "Keystore: {}.h5ks".format(store)
    print "Pass: {}".format(h)

def key(fn):
    f = file('{}.h5k'.format(fn),'w')
    f.write("-----BEGIN H5QL KEY-----\n")
    f.write(SECRET+"\n")
    f.write("-----END H5QL KEY-----\n")
    f.close()
    return


def encrypt(string, hkey):
    f = open('{}.h5k'.format(hkey), 'r')
    h = f.readlines()
    hh = base64.b64decode(h[1])
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    cipher = AES.new(hh)
    f.close()
    encoded = EncodeAES(cipher, string)
    return encoded


def decrypt(blob, hkey):
    f = open('{}.h5k'.format(hkey), 'r')
    h = f.readlines()
    hh = base64.b64decode(h[1])
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    cipher = AES.new(hh)
    decoded = DecodeAES(cipher, blob)
    return decoded
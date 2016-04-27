#
# Derived from: http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
#
import base64
from Crypto.Cipher import AES
from Crypto import Random

class AESCipher:
    BS = 16
    
    def __init__( self, key ):
        self.key = key[:32]
        
    def __pad(self, s): 
        return s + (AESCipher.BS - len(s) % AESCipher.BS) * chr(AESCipher.BS - len(s) % AESCipher.BS)
    
    def __unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
    
    def encrypt( self, raw ):
        raw = self.__pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 
    
    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return self.__unpad(cipher.decrypt( enc[16:] ))

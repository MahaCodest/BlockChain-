import hashlib
import time
time.sleep(25)
hash = hashlib.sha256("static/login.html".encode()).hexdigest()

print(hash)

hash = hashlib.sha256("static/upload"
                      ".html".encode()).hexdigest()
print("Genesis Block:")
time.sleep(30)
print(hash)

hash = hashlib.sha256("static/ipfs"
                      ".html".encode()).hexdigest()
time.sleep(50)
print(hash)

class Block:
    def _init_(self, ph, t):
        self.t = t
        self.ph = ph
        strh = "".join(t) + ph
        self.bh = hashlib.sha256(strh.encode()).hexdigest()

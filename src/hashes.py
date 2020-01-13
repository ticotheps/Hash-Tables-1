import time
import hashlib


n = 1000000
key = b"STR"

for _ in range(10):
  print(hash(key)) # Python's built-in 'hash()' function
print("\n")
  
for _ in range(10):
  print(hashlib.sha256(key)) # sha256 hash function
print("\n")
  
for _ in range(10):
  print(hashlib.sha256(key).hexdigest()) # enable visual for hash
print("\n")

for _ in range(10):
  print(int(hashlib.sha256(key).hexdigest(), 16)) # enable visual for 16 digits of hash
print("\n")

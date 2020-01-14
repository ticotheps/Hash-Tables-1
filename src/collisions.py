import random

def how_many_before_collisions(buckets, loops=1):
  """
  Roll random hashes into 'buckets' and print.
  'buckets' = index
  How many rolls before a hash collision?
  
  Run `loops` number of times
  """
  
  for _ in range(loops):
    tries = 0
    tried = set() # set = a dictionary that only stores keys
    
    while True:
      random_key = str(random.random())
      hash_index = hash(random_key) % buckets 
      
      if hash_index not in tried:
        tried.add(hash_index)
        tries += 1
      else:
        break
      
    print(f"\nBuckets: {buckets}\nHashes Before Collision: {tries} ({tries / buckets * 100:.1f}%)\n")
    
how_many_before_collisions(32, 10)
# %%
import hashlib
from datetime import datetime,timezone
import random
import string

def generate_random_string():
    size = 40
    allowed_chars = string.ascii_letters + string.punctuation
    return ''.join(random.choice(allowed_chars) for x in range(size))  


class Block:

    def __init__(self,data,previous_hash=0):
        self.timestamp = datetime.now(timezone.utc) #automatically create timestamp upon  block creation
        self.data = data # automatically generate text data from english letters and punctuation
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()


    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)
        
        sha.update(str(self.timestamp).encode('utf-8'))

        sha.update(str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.head = None
        self.num_blocks = 0
        self.tail = None  

    def appendblock(self,data):
        if self.head == None: #reference to start of chain
            self.head = Block(data)
            self.num_blocks += 1
            self.tail = self.head #reference to end of chain
        else:
            new_block = Block(data,previous_hash=self.tail.hash)
            self.num_blocks += 1
            self.tail = new_block


# %%
# Test 1
#create the block chain
chain = BlockChain()
chain.appendblock(generate_random_string())
chain.appendblock(generate_random_string())
chain.appendblock(generate_random_string())
print(chain.head)
#return address of chain.head
print(chain.num_blocks)
#return 3
print(chain.tail)
# return address of chain.tail (the last block added)
print(chain.head.timestamp)
#return time chain block was created

# %%
# Test 2
chain1 = BlockChain()
print(chain1.head)
print(chain1.num_blocks)
print(chain1.tail)

# %%
# Test 3
chain3 = BlockChain()
chain3.appendblock("one")
print(chain.tail.timestamp)
#return time crated which is same as the ones below
chain3.appendblock("two")
print(chain.tail.timestamp)
#return time crated which is same as the one above
chain3.appendblock("three")
print(chain.tail.timestamp)
#return time crated which is same as the ones above
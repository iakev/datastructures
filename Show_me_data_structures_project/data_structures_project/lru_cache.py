class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache_dict = {} # a dictionary to store the key-value pairs in the cache data structure.
        self.key_count = {} # a dictionary to associate a key with number of times it has been accessed
        self.num_entries = 0 # to keep track of number of items in our cache

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 

        if key in self.cache_dict:
            value = self.cache_dict[key]
            self.key_count[key] += 1  #to keep track of number of times a key is accessed/used
            return value
        
        
        return -1
        
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.num_entries < self.capacity:

            if key not in self.cache_dict:
                self.cache_dict[key] = value
                self.key_count[key] = 0
                self.num_entries += 1
        else: #we take advantage of the fact that dictionaries are insertion ordered to find the least recently used key-value pair.
            least_count = 1
            least_key = None
    
            for k,v in self.key_count.items():
                if v <= least_count:
                    least_count = v
                    least_key = k
                    if least_count == 0:
                        break

            del self.cache_dict[least_key]
            del self.key_count[least_key]
            self.cache_dict[key] = value
            self.key_count[key] = 0


## Test Cases ##

# Test case 1
cache = LRU_Cache(5)

cache.set(0,1)
cache.set(1,2)
cache.set(2,3)
cache.set(3,4)
cache.set(4,5)


print(cache.get(1)) 
#return 2
print(cache.get(2)) 
#return 3
print(cache.get(4)) 
#return 5
print(cache.get(10)) 
#return -1 since 10 not present
print(cache.get(1)) 
#return 2

cache.set(5,6) # overload the cache beyond set capacity
print(cache.get(5))
#return 6 since overload succesful
print(cache.get(0)) 
# return -1 since least used and earlier inserted key is discarded

# Test 2

cache2 = LRU_Cache(5)

cache2.set(0,1)
cache2.set(1,2)
cache2.set(2,3)
cache2.set(3,4)
cache2.set(4,5)
cache2.set(10,9) #set beyond capacity

print(cache2.get(0))
#return -1 since removed as oldest least recently used 
print(cache2.get(10))
# returns -1 since all previous keys are all least used hence cant add a new key

# Test 3

cache3 = LRU_Cache(5)

#input as string also valid
cache3.set("10",11)
cache3.set("11",12)
cache3.set("12",13)
cache3.set("13",14)
cache3.set("14",15)

print(cache3.get("10"))
# return 11 
print(cache3.get("11"))
# return 12
print(cache3.get("11"))
# return 12
print(cache3.get("12"))
# return 13
print(cache3.get("12"))
# return 13
print(cache3.get("13"))
# return 14
print(cache3.get("13"))
# return 14
print(cache3.get("13"))
# return 14
print(cache3.get("14"))
# return 15
print(cache3.get("14"))
# return 15
print(cache3.get("14"))
# return 15
print(cache3.get("14"))
# return 15
print(cache3.get("20"))
#return -1 since not present

cache3.set("20",21)

print(cache3.get("10"))
# returns -1 since key "10" least used hence discarded

print(cache3.get("20"))
# returns 21
cache3.set("25",26)

print(cache3.get("20"))
#return -1 since least recently used

print(cache3.get("25"))
#returns 26



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
            prev_count = 0
            for k in self.cache_dict:
                current_count = self.key_count[k]
                if current_count < prev_count:
                    del self.cache_dict[k]
                    del self.key_count[k]
                    self.cache_dict[key] = value
                    return

                prev_count = current_count
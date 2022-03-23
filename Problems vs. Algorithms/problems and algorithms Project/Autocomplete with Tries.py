# %%
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes_list = []
        
        suffixes = self.suffixes_helper(suffix,suffixes_list)
        if suffixes:
            return suffixes
        return "Word complete"

    def suffixes_helper(self,suffix,suffixes):
        #base _case 
        if self.children == {}:
            if self.is_word == True:
                suffixes.append(suffix) 
            return 

        for key in self.children:
            if self.is_word == True:
                if suffix not in suffixes:
                    suffixes.append(suffix)
            suffix += key
            self.children[key].suffixes_helper(suffix,suffixes)
            suffix = suffix[:len(suffix)-1]
            
        
        return suffixes

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
                continue
            node.insert(char)
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            
        return  node


# %%
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# %%
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');

# %%




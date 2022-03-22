 # %%
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
    
    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    # continue here by changing this logic to a recursive logic 
    def insert(self, path,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # path is a list containing path parts
        node = self.root

        # for part in path:
        #     if part in node.children:
        #         node = node.children[part]
        #         continue
        #     node.insert(part)
        #     node = node.children[part]

        # node.handler = handler

        ## recursive insert
        self.insert_path_recursively(path,handler,node)
        

    def insert_path_recursively(self,path,handler,node):

        # base case
        if len(path) == 0:
            node.handler = handler
            return 
        
        item = path.pop(0)

        if item == "":
            if "/" in node.children:
                node = node.children["/"]
            else:
                node.insert("/")
                node = self.root.children["/"]

        elif item in node.children:
            node = node.children[item]
        
        else:
            node.insert(item)
            node = node.children[item]

        self.insert_path_recursively(path,handler,node)    



    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        node = self.root
        if path == ["",""]: # root is the only path
            return node.handler


        for i in range(len(path)): 
            if path[i] == '' and i == 0:
                node = node.children['/']
                continue    
            if path[i] in node.children:
                node = node.children[path[i]]

            else:
                return None

        return node.handler

# %%
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler)

    def add_handler(self, path,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.router.insert(path_list,handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        return self.router.find(path_list)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        path_list = path.split('/')
        return path_list

# %%
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/blog/2019-01-15/my-awesome/blog", "This is the first post on my blog!!! Yeah I am excited.")

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/blog/2019-01-15/my-awesome/blog")) # should print "This is the first post on my blog!!! Yeah I am excited."

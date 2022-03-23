## Problem Statement
Create a Trie datastructure and use it to make a router to serve up content according to the matched url path.

### Design Consideerations
A dictionary eas used to implement the trie as it proved to be quite easy to visulaize and implement tries using a dictionary. However now the dictionary keys are separated and informed by `/`. We use `/` to separate the input path into separate keys to be added to a trie. The last key will contain the content of interest that when requested needs to be served up.

### Space and Time Complexity

For the *add handler* mehod the time complexity becomes `O(n)`,where `n` is the length of list created by splitiing path string at `/`.

Similarly for *lookup* method the complexity is `O(n)` where `n` is the length of list created by splitiing path string at `/`.

The space complexity for a trie creation is `O(m*n)`, where `m` is the numer of keys (path parts) created and `n` is the average length of keys (path part) in the trie.

Method 1 *add_handler*
Time and Space complexity - Since add handler has two more methods i.e. *split_path* and *insert* we individually look at the two:
- submethod 1 *split_path*
        -Time complexity - Has a runtime of `O(n)` where `n` is the number of contigous words before a `/`
        -Space complexity - Also consumes `O(n)` space with `n` representing the items in url path.

- submethod 2 *insert*
        -Time complexity - Has a runtime of `O(n)` where `n` is the number of items in the above created path.
        -Space complexity - Has a space complexity of  `O(n)` where `n` is the number of items in the above created path,when taken in modularity fashion.

hence the final runtime is `O(n)` and space consumed is also `O(n)`.

Method 2 *lookup*

Time and Space complexity - Since add handler has two more methods i.e. *split_path* and *find* we individually look at the two:
- submethod 1 *split_path*
    -Time complexity - Has a runtime of `O(n)` where `n` is the number of contigous words before a `/`
        -Space complexity - Also consumes `O(n)` space with `n` representing the items in url path.

- submethod 2 *find*
    - Time complexity - Has a runtime of `O(n)` where `n` is the number of items in path list created above
        - Space complexity since no other data structure is required during this method's implementation there is a space complexity of `O(1)`

Hence in a overall sense the Time complexity becomes `O(n)` and also a space complexity of `O(n)`. 


Method 3 *split_path*

Since this is a helper function utilized by both *lookup* and *add_handler* we have already discussed it's complexities.
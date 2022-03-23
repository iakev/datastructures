## Problem Statement
Create a Trie datastructure and use it to make an autocomplete function given some words.

### Design Consideerations
A dictionary ease used to implement the trie as it proved to be quite easy to visulaize and implement tries using a dictionary.

### Space and Time Complexity

Method 1 *insert*
Time complexity - This will take `O(n)`. Where `n` is the length of word being inserted.
Space complexity - Space complexity will be `O(m*n)`, where `m` is the numer of keys created and `n` is the average length of keys in the trie in this case the length of words..

Method 2 *find*
TIme complexity - This will take `O(n)`. Where `n` is the number of characters in the *prefix* node.
Space complexity - Since no extra data structure is created for this method we have `O(1)` space complexity.

method 3 *suffixes*
Time complexity - This will take `O(n*m)` where `n` represents the number of children in a certain prefix node while `m` represents keys in a certain child of a prefix node.
Space complexity - Space consumed by this method is `O(m)` where `m` represents the number of keys of all children of a prefix node. There is also  `O(n)` where `n` is the length of resulting suffixes list.
Hence the total space complexity is linear `O(N) = O(m) + O(n)`. 
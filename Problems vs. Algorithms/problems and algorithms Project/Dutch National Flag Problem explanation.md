## Problem Statement
Given an array containing only 0's,1's and 2's perform an in-place sorting algorithm that traverses the input array only once. Hence time complexity is `O(n)`.

### Design Considerations
The basic idea is that by sorting all the *zeros* and *two's* accurately then the ones are automatically sorted. Hence to achieve this two pointers to keep track of *zeros* and *twos* were used.

### Space and Time Complexity.
The space complexity of the algorithm was `O(1)` since no extra space was utilized during algorithm implementation.

The time complexity was `O(n)` since a complete traversal of the array was performed albeit once.
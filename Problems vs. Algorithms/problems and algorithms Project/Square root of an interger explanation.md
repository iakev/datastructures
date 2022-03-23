## Problem Statement
For this problem one should find the square root of an interger without using any python library. We are concerned with the floor value of the square root. The time complexity for the square root should be `O(log n)`.

### Design Considerations
So to find this square root I decided to use binary search algorithm and just created a list of length `number` (input to the sqrt function). So from the list the floor value of square root is found by halfing the list size at each iteration.

### Space and Time Complexity
Space complexity used in recursive binary search is `O(log n)`, since the binary search implemented is in-place. Hence the total space complexity becomes `O(log n)`.

Time complexity for this algorithm is `O(log n)` since this is the complexity for a binary search algorithm.
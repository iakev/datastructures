## Problem Statement
Find the minimum and maximum elements in an unsorted array,without sorting and ensure time complexity is `O(n)`.

### Design Considerations
Using divide and conquer technique specifically *fastselect* for any kth element in the array we can achieve the specified complexity. This is helped by calling *fastselect* for the smallest and again for the largest element.

### Space and Time complexity

Time complexity will be `O(n)`. Since for any fast select we have `O(n)` time complexity and `O(n)` + `O(n)` = `O(n)`.

Space complexity will also be `O(n)`. Since I use a dictionary to store lists of length $\frac{n}{5}$ which add upto to size `n`. Also the three arrays around the pivot also add up to `n`. Hence, `O(n) + O(n) + O(n)` = `O(n)`.
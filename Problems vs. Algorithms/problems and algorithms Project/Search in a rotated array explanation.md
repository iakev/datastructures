## Problem Statement
We are given a sorted array rotated at a random pivot point. The goal is to find a given target's value index and if not present return -1. We assume no duplicates are given and are constrained to a time complexity of `O(log n)`.

### Design considerations
Due to the constraint given of time complexity of `O(log n)`. I decided to use the binary search algorithm to solve the problem. It was the same algorithm however I needed to pay close attention to elements immediately before and after the mid element.

### Time and Space Complexity
Space complexity used in this algorithm is `O(log n)`, since the binary search implemented is in-place.However since the implementation is not iterative ehich has a case of `O(1)` due to the recusrsive stack we end up with a space complexity of `O(log n)`.

Time complexity for the solution is `O(log n)`. since we half the input size every time as in every binary search algorithm.
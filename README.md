# foobar
Foobar solutions

## When it rains, it pours
This solution is in Python. It operates much like a binary search, except it searches for wells.

For example, [3, 4, 5, 1, 2, 3, 1] would be split into two arrays: [3, 4, 5] and [5, 1, 2, 3, 1]. Then, each of those arrays may be split as necessary. [3, 4, 5] would be split into [3, 4] and [4, 5], neither of which get filled. [5, 1, 2, 3, 1] would become [5, 1, 2, 3] which would be filled, and [3, 1] which would not be filled. 

## Pirates
This solution is in Python. Returns the number of pirates which form a loop, given that you start by talking to the left-most pirate, 0. 

For example, suppose the numbers list were [1, 3, 0, 1]. Then pirate 0 redirects to pirate 1, who redirects to pirate 3, who redirects back to pirate 1. There is a loop of two pirates: 1, 3. Thus the answer would be 2. Note that even though you started with pirate 0, he is not part of the loop.

## Zombit Monitoring
This solution is in Python. Takes a list of pairs [start, end] and returns the total amount of time that Dolly the Zombit was monitored by at least one minion. Each [start, end] pair represents the times when a minion started and finished monitoring the zombit. 
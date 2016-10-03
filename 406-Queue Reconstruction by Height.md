# Code

## Description
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

## Python Solution
```
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people = sorted(people, key=operator.itemgetter(0))

        output = [None] * len(people)
        for i in range(len(people)):
            count_left = people[i][1]
            for j in range(len(people)):
                if count_left == 0 and output[j] is None:
                    output[j] = people[i]
                    break
                if output[j] is None or people[i][0] <= output[j][0]:
                    count_left -= 1
        return output

```

## Some thinking

First we need an order to reconstruct this queue and then put each of people into the right place.

I decide sort it by height in ascending order. I am going to put each people "i" in some position such that there is enough room for demanding number of taller people in front of i.

To achieve this, each time I need to iterate the reconstructed queue. for position i: if no people standing there, we left this position for taller people that we'll put in later and see next position i+1; if a taller people has already been standing there, then we go to see the next place i+1, until we have reserved enough position.

Why sort by height:

beacause if we first set the position for shorter people a, then the postion we set for coming taller people b will not affect a. (if we put him in front of a, it fills the slot that a has reserved for taller people like b)

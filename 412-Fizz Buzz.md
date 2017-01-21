# Code

## Description

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

## Python Solution
```
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lists = []
        for i in range(1, n + 1):
            num = ""
            if i % 3 and i % 5:
                num = str(i)
            else:
                if i % 3 == 0:
                    num = num + "Fizz"
                if i % 5 == 0:
                    num = num + "Buzz"
            lists.append(num)
        return lists
```

more cleaner:
```
return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
```

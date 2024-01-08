"""Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

**Example 1:**

Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.
5%2 ==1 and 5%5 ==0
6%2 ==0 and 6%5 ==1

10%2==0 and 10%5==0 so 10 is smallest positive integer both 5 and 2

**Example 2:**

Input: n = 6
Output: 6
Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
6%2 ==0 and 6%6 ==0"""


def smallestEvenMultiple(self, n: int) -> int:
    if n % 2 == 0:
        return (n)
    else:
        return (n * 2)
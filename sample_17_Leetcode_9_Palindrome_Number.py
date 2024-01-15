"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        low = 0
        upper = len(str(x)) - 1
        flag = 0
        while (low < upper):
            if (str(x)[low] != str(x)[upper]):
                return False
                flag = 1
                break
            low += 1
            upper -= 1
        if flag == 0:
            return True

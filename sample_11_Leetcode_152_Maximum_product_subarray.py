"""
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


def maxProduct(nums):
    curMax, curMin = 1, 1
    res = 0

    for n in nums:
        vals = (n, n * curMax, n * curMin)
        print(vals)
        curMax, curMin = max(vals), min(vals)
        print(curMax,curMin)
        res = max(res, curMax)
        print(res)

    print(res)
nums = [-2]
maxProduct(nums)


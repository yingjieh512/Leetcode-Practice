class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        case1 = nums[-1] * nums[-2] * nums[-3]
        case2 = nums[0] * nums[1] * nums[-1]

        return max(case1, case2)


"""
Problem:
Given an integer array nums, choose three numbers whose product is as
large as possible and return that maximum product.


Solution / Explanation:
After sorting nums from smallest to largest, there are only two cases
that can produce the maximum product.

Case 1:
Use the three largest numbers:

    nums[-1] * nums[-2] * nums[-3]

For example:

    [1, 2, 3, 4]

The best product is:

    2 * 3 * 4 = 24


Case 2:
Use the two smallest numbers and the largest number:

    nums[0] * nums[1] * nums[-1]

Why?

The two smallest numbers may both be very negative.
Multiplying two negative numbers produces a large positive number.

Example:

    [-10, -10, 1, 2, 3]

Three largest numbers:

    1 * 2 * 3 = 6

Two smallest numbers and largest number:

    (-10) * (-10) * 3 = 300

So we only need to compare these two possibilities.


Why absolute-value sorting is unnecessary:
If we sort by absolute value, we still need to carefully track signs.

For example:

    [-10, -10, 1, 2, 3]

The numbers with the largest absolute values are:

    -10, -10, 3

which works here.

But in other cases, taking the three largest absolute values may produce
a negative product even though a smaller positive product exists.

Example:

    [-10, 2, 3, 4]

Three largest absolute values are:

    -10, 4, 3

Product:

    -120

But the real maximum is:

    2 * 3 * 4 = 24

Therefore, it is much simpler to sort normally and compare the only two
possible optimal forms.


Time Complexity:
O(n log n)

because sorting takes O(n log n).


Space Complexity:
O(1) extra space, ignoring the internal space used by Python's sorting.
"""
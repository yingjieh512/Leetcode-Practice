class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()

        min_diff = float('inf')
        result = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]

            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result


"""
Problem:
Given an array of distinct integers, find all pairs of numbers with the
minimum absolute difference.

Each returned pair [a, b] must satisfy:
- a < b
- b - a is the minimum absolute difference among all pairs
- The result should be in ascending order


Solution / Explanation:
First sort the array.

After sorting, the minimum absolute difference must occur between two
adjacent elements.

For example:

    [1, 4, 7, 10]

There is no need to compare 1 and 7, because 4 is between them.
The difference 7 - 1 must be larger than at least one adjacent difference:

    4 - 1
    7 - 4

Therefore, after sorting, we only need to compare:

    arr[i] - arr[i - 1]

for every adjacent pair.

We keep:

    min_diff

as the smallest difference found so far, and:

    result

as all pairs having that difference.

If:

    diff < min_diff

we found a new smaller difference. This means all previously stored pairs
are no longer valid, so we update min_diff and reset result:

    min_diff = diff
    result = [[arr[i - 1], arr[i]]]

If:

    diff == min_diff

the current pair has the same minimum difference, so we add it:

    result.append([arr[i - 1], arr[i]])

We do not need to worry that a smaller difference may appear later.

If a smaller difference appears later, the condition:

    diff < min_diff

will replace the old min_diff and completely reset result.

Example:

    arr = [1, 5, 8, 10]

Check adjacent pairs:

    5 - 1 = 4
    min_diff = 4
    result = [[1, 5]]

    8 - 5 = 3
    3 < 4

So the previous answer is discarded:

    min_diff = 3
    result = [[5, 8]]

Then:

    10 - 8 = 2
    2 < 3

Again reset:

    min_diff = 2
    result = [[8, 10]]

So one traversal is enough because we continuously maintain the best
answer found so far.


Time Complexity:
O(n log n)

Sorting takes O(n log n), and scanning the array takes O(n).


Space Complexity:
O(n)

The returned result can contain up to O(n) pairs.
"""
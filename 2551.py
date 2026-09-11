class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """

        if k == 1:
            return 0

        pair_sums = []

        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i + 1])

        pair_sums.sort()

        min_score = sum(pair_sums[:k - 1])
        max_score = sum(pair_sums[-(k - 1):])

        return max_score - min_score


"""
Problem:
We need to divide the marbles into k non-empty contiguous bags.
If a bag contains marbles from index i to j, its cost is
weights[i] + weights[j].

We need to return the difference between the maximum possible
total score and the minimum possible total score.

Solution:
To divide the array into k bags, we need to make exactly k - 1 cuts.

Suppose we cut between index i and i + 1.

Before the cut, those two positions are inside the same segment.
After the cut:
- weights[i] becomes the last marble of the left bag
- weights[i + 1] becomes the first marble of the right bag

Therefore, this cut contributes:

    weights[i] + weights[i + 1]

to the total score.

The first marble weights[0] and the last marble weights[-1]
are always included in the score regardless of where we cut,
so they cancel out when calculating maximum_score - minimum_score.

Therefore:
1. Compute the cost of every possible cut:
       weights[i] + weights[i + 1]
2. Sort all cut costs.
3. For the minimum score, choose the smallest k - 1 cut costs.
4. For the maximum score, choose the largest k - 1 cut costs.
5. Return their difference.

Example:
weights = [1, 3, 5, 1], k = 2

Possible cut costs:
1 + 3 = 4
3 + 5 = 8
5 + 1 = 6

Sorted:
[4, 6, 8]

We need 1 cut because k - 1 = 1.

Minimum uses 4.
Maximum uses 8.

Answer = 8 - 4 = 4.

Time Complexity:
O(n log n), because we sort the n - 1 possible cut costs.

Space Complexity:
O(n), for storing the cut costs.
"""
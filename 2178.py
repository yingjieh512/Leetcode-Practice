class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """

        used_rows = set()
        used_cols = set()

        ans = 0

        for i in range(len(queries) - 1, -1, -1):
            typei = queries[i][0]
            indexi = queries[i][1]
            vali = queries[i][2]

            if typei == 0:
                # 如果这行已经被后面的 query 覆盖过
                if indexi in used_rows:
                    continue

                ans += vali * (n - len(used_cols))
                used_rows.add(indexi)

            else:
                # 如果这列已经被后面的 query 覆盖过
                if indexi in used_cols:
                    continue

                ans += vali * (n - len(used_rows))
                used_cols.add(indexi)

        return ans
"""
2718. Sum of Matrix After Queries
Solved
Medium
Topics
conpanies icon
Companies
Hint
You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].

Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:

if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
Return the sum of integers in the matrix after all queries are applied.

 

Example 1:


Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
Output: 23
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23. 
Example 2:


Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
Output: 17
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 17.
 

Constraints:

1 <= n <= 104
1 <= queries.length <= 5 * 104
queries[i].length == 3
0 <= typei <= 1
0 <= indexi < n
0 <= vali <= 105
"""
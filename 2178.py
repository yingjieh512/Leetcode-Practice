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
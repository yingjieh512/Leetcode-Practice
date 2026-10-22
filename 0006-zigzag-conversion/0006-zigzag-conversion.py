class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        rows = [""] * numRows
        row = 0
        direction = 1  # 1 表示向下，-1 表示向上

        for char in s:
            rows[row] += char

            if row == 0:
                direction = 1       # 到顶，转向下
            elif row == numRows - 1:
                direction = -1      # 到底，转向上

            row += direction

        return "".join(rows)
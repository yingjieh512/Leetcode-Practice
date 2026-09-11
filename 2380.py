class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = list(s)
        seconds = 0

        while True:
            changed = False
            i = 0

            while i < len(s) - 1:
                if s[i] == '0' and s[i + 1] == '1':
                    s[i], s[i + 1] = '1', '0'
                    changed = True
                    i += 2
                else:
                    i += 1

            if not changed:
                break

            seconds += 1

        return seconds


"""
Problem:
Given a binary string s.

Every second, all occurrences of "01" are simultaneously replaced
with "10".

Repeat this process until there is no "01" left.

Return the number of seconds needed.


Solution / Explanation:
The most direct solution is simulation.

For every second:
1. Traverse the string from left to right.
2. Whenever we find "01", swap it into "10".
3. Since all swaps in the same second must happen simultaneously,
   after swapping positions i and i + 1, we skip both positions by:

       i += 2

   This prevents a newly created character from being swapped again
   during the same second.

4. If an entire traversal makes no changes, there is no "01" left,
   so the process is finished.

Example:

    s = "0110101"

During each second, every valid "01" moves the 1 one position
to the left.

Eventually all 1s will be on the left and all 0s will be on the right:

    1111000

At that point there is no "01" remaining.


Time Complexity:
O(n^2) in the worst case.

We may need O(n) seconds, and each second scans O(n) characters.


Space Complexity:
O(n)

Python strings are immutable, so we convert s into a list.
"""
        
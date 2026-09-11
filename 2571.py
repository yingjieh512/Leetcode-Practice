class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """

        operations = 0

        while n > 0:

            if n % 2 == 0:
                n >>= 1

            else:
                if n == 1 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1

                operations += 1

        return operations


"""
Problem:
We can add or subtract any power of 2 from n.

Return the minimum number of operations needed to make n equal to 0.


Solution / Explanation:
Think about n in binary.

Adding or subtracting a power of 2 means changing one binary position.

We process the binary number starting from the least significant bit.

If the last bit is 0:

    ...0

there is nothing to remove at this position.
We can simply shift right:

    n >>= 1

This does not count as an operation because shifting is only part of
our algorithm, not an actual operation performed on n.


If the last bit is 1, we must eventually remove it.

There are two important cases.

Case 1:
The last two bits are:

    01

The lowest 1 is isolated.

It is best to subtract 1:

    ...01
       -1
    -----
    ...00

So:

    n -= 1


Case 2:
The last two bits are:

    11

There are consecutive 1s.

Instead of subtracting each 1 separately, it is usually better to add 1.

For example:

    00111
  + 00001
  -------
    01000

Adding 1 causes the consecutive 1s to carry into a higher bit,
turning many 1s into zeros at once.

So when the last two bits are 11:

    n += 1


We can inspect the last two bits using:

    n & 3

because:

    3 = 0b11

Therefore:

    n & 3 == 1   means the number ends in 01
    n & 3 == 3   means the number ends in 11


Special case:
When n == 1, we should simply subtract 1 and finish.


Example:

    n = 39
    binary = 100111

The number ends in 11, so add 1:

    100111 + 1 = 101000

operations = 1

Remove trailing zeros by shifting:

    101

Now it ends in 01, so subtract 1:

    101 - 1 = 100

operations = 2

Shift away the zeros:

    1

Finally subtract 1:

    1 -> 0

operations = 3

Therefore the answer is 3.


Time Complexity:
O(log n)

We process approximately one binary digit at a time.


Space Complexity:
O(1)
"""
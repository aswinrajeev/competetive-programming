"""
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.

"""


# Sub-optimal: Time limit exceeded
class Solution:
    """
    Solve using a sliding window
    """

    def minSwaps(self, nums: List[int]) -> int:
        self.nums = nums

        # Window size = max number of ones - like an electron and holes, where remaining 1s are left to fill the holes
        window_size = total_count_of_ones = nums.count(1)
        min_swaps_required = count

        for i in range(0, len(nums)):
            # Calculate the # of 1s in this window
            curr_count_of_ones = self.sum(i, window_size)
            ## TODO: Instead of computing sum for every iteration, reduce the element going out and add the element coming in

            # The diff between total 1s and the 1s in the window = holes, which can be filled by swapping
            min_swaps_required = min(
                min_swaps_required, total_count_of_ones - curr_count_of_ones
            )

        return min_swaps_required

    def sum(self, start: int, window_size: int):
        """
        Calculate the sum of a window in a circular list
        """

        sum = 0
        for i in range(start, start + window_size):
            sum += self.nums[
                i % len(self.nums)
            ]  # (i % len) would give the element from the start if window overflowing

        return sum

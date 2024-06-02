class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c1 = 0
        c2 = 0

        if m == 0:
            del nums1[-1 * n :]
            nums1.extend(nums2)
            return
        elif n == 0:
            return

        while True:
            print(f"{c1}, {c2}")
            if c1 == m + n or c2 == n:
                break

            if nums1[c1] > nums2[c2] or c1 >= m + c2:
                del nums1[-1]
                nums1.insert(c1, nums2[c2])
                c2 += 1
            c1 += 1

    def merge_optimal(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        pointer = len(nums1) - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[pointer] = nums1[m - 1]
                m -= 1
            else:
                nums1[pointer] = nums2[n - 1]
                n -= 1
            pointer -= 1

        # If all elements in nums1 are larger than remaining elements in num2,
        #   simply add those in the beginning
        while n > 0:
            nums1[pointer] = nums2[n - 1]
            n -= 1
            pointer -= 1

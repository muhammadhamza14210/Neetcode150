class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in nums:
                streak = 0
                while (n + streak) in set_num:
                    streak += 1
                longest = max(longest, streak)
        
        return longest

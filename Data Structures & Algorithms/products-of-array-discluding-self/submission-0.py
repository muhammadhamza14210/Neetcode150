class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            ans = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                ans *= nums[j]
            output.append(ans)
        return output
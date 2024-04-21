class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        majelement = 0


        for i in range(n):
            if count == 0:
                majelement = nums[i]
            if majelement == nums[i]:
                count += 1
            else:
                count -= 1
   
        chkCount = 0

        for i in range(n):
            if majelement == nums[i]:
                chkCount += 1
        if chkCount > n // 2:
            return majelement
        return -1
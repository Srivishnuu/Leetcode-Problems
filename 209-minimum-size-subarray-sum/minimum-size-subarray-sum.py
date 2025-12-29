class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        mini=10000000000
        subsum=0
        while r < len(nums):
            subsum += nums[r]
            
            while subsum >= target:
                mini =min(mini,r-l+1)
                subsum -=nums[l]
                l +=1

            r+=1
            
        return 0 if mini == 10000000000 else mini

        
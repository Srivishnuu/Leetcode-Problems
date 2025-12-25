class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        a=set()
        l,r = 0,len(nums)-1
        while l<r:
            a.add((nums[l]+nums[r])/2)
            l+=1
            r-=1
        return len(a)


        
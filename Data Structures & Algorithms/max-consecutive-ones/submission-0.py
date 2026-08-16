class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        count=0
        max_count=0
        length=len(nums)
        while(i<length):
            if nums[i]==1:
                count+=1
                i+=1
            else:
                if count > max_count:
                    max_count = count
                count=0
                i+=1
    
        return max(max_count, count)
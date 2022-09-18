class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left = 0 
        right = length-1

        
        while left<right:
            mid =left+(right-left)//2
            if nums[right]<nums[mid]: #[4,5,6,7,1,2,3]
                left = mid +1   
            else :
                right = mid
                
        return nums[left]
    
#Using library

# class Solution:
#     def findMin(self, nums):
#         self.__getitem__ = lambda i: nums[i] <= nums[-1]
#         return nums[bisect.bisect(self, False, 0, len(nums))]    
    
    
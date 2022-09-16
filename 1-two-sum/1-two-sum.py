class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i
		
		# An Upvote will be encouraging
    
    
#         j = 1
        
#         for i in range(len(nums)):
#             while j < len(nums):
#                 if(nums[i] + nums[j] == target):
#                     return [i,j]
#                 else:
#                     j += 1
#             i += 1
#             j = i+1
            
            
            
#map 사용시 exception 사용하기
#target-num의 나머지 
#나중에 중복이 많아지면 put에 시간이 오래걸리게 되면 if statement를 넣는게 더 빠를수도 
#지금은 o(n^2)이지만 해시맵을 쓰면 o(n)안에 풀 수 있음. 
#map이랑 set 공부하기 장단점 등등 

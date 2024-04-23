#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:      
        #solution 1 (myself) - bruteforce - O(n^2)
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return[i,j]
                    
        #solution 2 (solution) - two pass hash table - O(2n)
        n = len(nums)
        numMap = {}
        
        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i,numMap[complement]]
        
        #solution 3 (solution) - one pass hash table - O(n)
        numDict = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in numDict:
                return[numDict[diff],index]
            numDict[number] = index
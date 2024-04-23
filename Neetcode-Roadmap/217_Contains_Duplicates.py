#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #solution 1 (myself) - bruteforce - O(n^2)
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True;
        return False;

        #solution 2 (solution) - sort the list - O(n log n)
        nums.sort()
        n = len(nums)
        for index in range(n-1):
            if nums[index] == nums[index-1]:
                return True
        return False

        #solution 3 (solution) - hash set - O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
# Simple
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """     
        for i in range(len(nums)):
            left = nums[i+1:]
            for j in range(len(left)):
                if (nums[i] + left[j]) == target:
                    return i, j+i+1


# Two-pass Hash Table
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """     
        hash_table={}
        for i in range(len(nums)):    # make a hash table first
            hash_table[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in hash_table:
                if hash_table[target-nums[i]] != i:
                    return [i, hash_table[target-nums[i]]]
        return []


# One-pass Hash Table
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """     
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return([hash_table[target - num], i])
                break    # someone add break here, which make Runtime faster!!
            hash_table[num] = i
        return([])
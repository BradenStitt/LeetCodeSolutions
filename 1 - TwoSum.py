# 1. TwoSum Runtime 60 ms - Beats - 81.43% | Memory 15.1 MB - Beats 56.20%
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val : index

        # iterate through the list, first we subtract the difference of the target and the current value n at index i
        for i, n in enumerate(nums):
            difference = target - n 

            # if the difference is already in the hashmap, 
            # we have a sum that equals target so return that index hashmap[difference],
            # and the current index i
            if difference in hashmap:
                return [hashmap[difference], i]

            # if difference is not in hashmapm, add the index i into the hashmap at key n which is the value 
            hashmap[n] = i
        return

            

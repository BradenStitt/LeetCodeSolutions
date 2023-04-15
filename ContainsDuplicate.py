class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create hashset
        hash = set()
        
        # Iterate through hashset
        for i in nums:
            if i in hash: # if i is duplicate we return True
                return True
            hash.add(i) # if it's not duplicate, we add to the hashset and continue iteration

        return False # return false if no duplicates found

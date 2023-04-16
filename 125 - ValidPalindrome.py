class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two-pointer approach, left pointer and right pointer initialized
        l, r = 0, len(s) - 1

        # Continue checking until pointers cross
        while l < r:
            if not s[l].isalnum(): # if the left character is not alphanumeric, increment again
                l += 1
            elif not s[r].isalnum(): # if the right character is not alphanumeric, increment again
                r -= 1
            else:
                # if they are both alphanumeric but not equal then it is not palindrome
                if s[l].lower() != s[r].lower(): 
                    return False
                # if they are equal, then increment again and keep checking
                else: 
                    l += 1
                    r -= 1
        return True

                
            

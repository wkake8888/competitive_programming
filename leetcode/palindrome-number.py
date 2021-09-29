class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = list(str(x))
        reversed_x = list(reversed(str_x))
        if str_x == reversed_x:
            return True
        else:
            return False
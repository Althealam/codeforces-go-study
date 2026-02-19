class Solution:
    def isPalindrome(self, s: str) -> bool:
        # store all lower char element
        s_list = []
        for char in s:
            if char.isalpha():
                s_list.append(char.lower())
            elif char.isdigit():
                s_list.append(char)
        # valid palindrome
        left, right = 0, len(s_list)-1
        while left<right:
            if s_list[left]!=s_list[right]:
                return False
            else:
                left+=1
                right-=1
        return True
        
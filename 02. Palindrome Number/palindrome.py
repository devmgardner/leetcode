#https://leetcode.com/problems/palindrome-number/submissions/
class Solution:
    def isPalindrome(self, x):
        if list(str(x)) == list(reversed(list(str(x)))):
            return True
        else:
            return False
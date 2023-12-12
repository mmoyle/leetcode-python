
# palindrome problems probably use a reverse procedure

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))

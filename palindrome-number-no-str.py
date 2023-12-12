
# palindrome problems probably use a reverse procedure

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reverse  = 0

        while x > 0:
            # get last digit
            digit = x % 10
            # add the digit in the correct oder of magnitude
            reverse = reverse * 10 + digit
            # reduce order of magnitude of x
            x = x // 10

        return original == reverse

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))

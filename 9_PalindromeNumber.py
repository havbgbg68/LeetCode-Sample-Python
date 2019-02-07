class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        list_x = list(str(x))
        len_x = len(list_x)
        result = True
        for i in range(len_x//2):
            if list_x[i] != list_x[len_x-1-i]:
                result = False
                break

        return result
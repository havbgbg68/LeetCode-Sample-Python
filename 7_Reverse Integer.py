class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        num_list =[]

        if x>0:
            while x>0:
                num_list.append(x%10)
                x = int(x / 10)
        else:
            while x<0:
                num_list.append(x%-10)
                x = int(x / 10)
        digit = len(num_list)
        for i in range(digit):
            num = num + num_list[i] * (10**(digit-i-1))
            
        if num < -2**31 or num > (2**31 - 1):
            return 0
        else:
            return num
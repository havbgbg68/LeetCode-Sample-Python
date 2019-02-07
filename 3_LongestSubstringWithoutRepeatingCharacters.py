class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = []
        a =[]
        for i in s:
            if i in a:
                max_length.append(len(a))

                if i==a[-1]:
                    a=[i]
                else:
                    a=[]
            else:
                a.append(i)

        if a!=[]:
            max_length.append(len(a))

        if max_length:
            return max(max_length)
        else: 
            return 0
        
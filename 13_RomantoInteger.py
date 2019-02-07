class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': -2, # 4-1-5
            'IX': -2, # 9-1-10
            'XL': -20, # 40-10-50
            'XC': -20, # 90-10-100
            'CD': -200, # 400-100-500
            'CM': -200, # 900-100-1000
        }
        

        result = 0
        
        trans_list_1 = ['IV','IX','XL','XC','CD','CM']
        
        for i in trans_list_1:
            if i in s:
                result += trans_dict[i]
        for i in s:
            result += trans_dict[i]

        return result
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = {
            '(':')',
            '[':']',
            '{':'}',
        }
        a_keys = list(a.keys())
        table=[]
        res = False
        if len(s)%2!=0:
            
            return False
        for i in s:
            if table!=[] and i==table[-1]:
            
                # if :
                table = table[:-1]
            elif i in a_keys:
            
                table += a[i]
            else:
            
                table = ['f']
                res = False
                break
        if table==[]:
            res = True
        
        return res
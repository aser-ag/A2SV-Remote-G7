class Solution:    
    def findUnion(self, a, b):
        # code here
        c = a + b
        c_set = set(c)
        
        c = list(c_set)
        
        return c
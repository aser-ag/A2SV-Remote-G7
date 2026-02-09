#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        frequency = {}
        
        for num in a:
            frequency[num] = frequency.get(num, 0) + 1
        
        for num in b:
            if num not in frequency:
                return False
        
        return True
    
    

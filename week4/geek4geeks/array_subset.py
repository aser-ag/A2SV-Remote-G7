#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        frequency = {}
        
        for num in a:
            frequency[num] = frequency.get(num, 0) + 1
        
        for num in b:
            if num not in frequency or frequency[num] < 1:
                return False
            else:
                frequency[num] -= 1
        return True
    
    
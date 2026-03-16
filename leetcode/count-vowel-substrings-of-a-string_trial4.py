class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = {"a","e","i","o","u"}
        n = len(word)
        count = 0
        
        for i in range(n):
            window = set()
            
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                
                window.add(word[j])
                
                if len(window) == 5:
                    count += 1
        
        return count
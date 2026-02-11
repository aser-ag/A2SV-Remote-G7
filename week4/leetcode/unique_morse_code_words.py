class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        frequency = {}

        for word in words:
            transformation = []

            for char in word:
                index = ord(char) - 97
                transformation.append(morse[index])
                
            res = "".join(transformation)

            frequency[res] = frequency.get(res, 0) + 1


        return len(frequency.keys())
        
        



class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = Counter(words[0])
    
        for word in words[1:]:
            word_counter = Counter(word)

            for char in list(common.keys()):
                if char in word_counter:
                    common[char] = min(common[char], word_counter[char])
                else:
                    del common[char]
    
        result = []

        for char, count in common.items():
            result.extend([char] * count)
    
        return result
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        indices = {}
        n = len(score)
        ranks = [""] * n

        for i in range(n):
            indices[score[i]] = i
        
        keys_sorted = sorted(indices.keys(), reverse=True)

        for i in range(n):
            score = keys_sorted[i]
            index = indices[score]
            
            if i == 0:
                ranks[index] = "Gold Medal"
            elif i == 1:
                ranks[index] = "Silver Medal"
            elif i == 2:
                ranks[index] = "Bronze Medal"
            else:
                ranks[index] = str(i + 1)

        return ranks
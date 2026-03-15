class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        max_possible = 0

        left = 0
        types = {}
        best_sum = 0
        current = 0

        for right in range(len(fruits)):
            types[fruits[right]] = types.get(fruits[right], 0) + 1
            current += 1

            while len(types) >= 3:
                types[fruits[left]] -= 1
                if types[fruits[left]] == 0:
                    del types[fruits[left]]
                left += 1
                current -= 1
            
            best_sum = max(current, best_sum)
        
        return best_sum
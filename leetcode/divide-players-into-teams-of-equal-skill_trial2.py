class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        team_size = n / 2.0
        left, right = 0, n - 1
        skill.sort()
        total = sum(skill)
        target = total / team_size
        res = 0
        count = 0

        while left < right:
            if skill[left] + skill[right] == target:
                res += skill[left] * skill[right]
                left += 1
                right -= 1
                count += 1
            elif skill[left] + skill[right] < target:
                left += 1
            else:
                right -= 1
        
        if count != team_size:
            return -1
        else:
            return res
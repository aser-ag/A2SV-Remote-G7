class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        target_x = target[0]
        target_y = target[1]

        origin_to_target = abs(target_x) + abs(target_y)

        for ghost in ghosts:
            ghost_x = ghost[0]
            ghost_y = ghost[1]

            ghost_to_target = abs(ghost_x - target_x) + abs(ghost_y - target_y)
            
            if origin_to_target >= ghost_to_target:
                return False
        
        return True
        
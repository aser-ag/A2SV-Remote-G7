class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {}
        index_sum = {}
        ans = []

        for i in range(len(list1)):
            index_map[list1[i]] = i
        
        for i in range(len(list2)):
            string = list2[i]
            if string in index_map:
                index_sum[string] = i + index_map[string]
        
        least = min(index_sum.values())
        
        for key in index_sum:
            if index_sum[key] == least:
                ans.append(key)
        
        return ans
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        st = [ord(char) - ord('a') for char in s]
        
        diff = [0] * (n + 1)

        diff[0] = st[0]
        for i in range(1, n):
            diff[i] =  st[i] - st[i - 1]
        
        for shift in shifts:
            left, right, direction = shift[0], shift[1], shift[2]

            if direction == 1:
                diff[left] += 1
                diff[right + 1] -= 1
            else:
                diff[left] -= 1
                diff[right + 1] += 1
        
        result = [0] * n
        result[0] = diff[0]

        for i in range(1, n):
            result[i] = result[i - 1] + diff[i]
        
        for i in range(n):
            char = (result[i] % 26) + ord('a')
            st[i] = chr(char)
        
        return "".join(st)
        
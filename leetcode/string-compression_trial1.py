class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left, right = 0, 0
        n = len(chars)
        res = []
        stop = 0
        while right < n:
            count = 0
            while right < n and chars[left] == chars[right]:
                right += 1
                count += 1

            if count == 1:
                chars[stop] = chars[left]
                stop += 1
            else:
                chars[stop] = chars[left]
                stop += 1
                for num in str(count):
                    chars[stop] = num
                    stop += 1
            left = right

        i = n - 1
        while i >= stop:
            chars.pop()
            i -= 1
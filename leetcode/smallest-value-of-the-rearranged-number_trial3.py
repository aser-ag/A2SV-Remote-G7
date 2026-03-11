class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num > 0:
            digits = sorted(list(str(num)))

            if digits[0] == "0":
                next_non_zero = 1

                while digits[next_non_zero] == "0" and next_non_zero < len(digits):
                    next_non_zero += 1

                digits[0], digits[next_non_zero] = digits[next_non_zero], digits[0] 

            return int("".join(digits))

        else:
            digits = sorted(list(str(num)), reverse=True)

            return int("".join(digits[:-1])) * -1
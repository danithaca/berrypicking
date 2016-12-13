class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        else:
            first_list = digits[:-1]
            last_digit = digits[-1]
            if last_digit == 9:
                l = self.plusOne(first_list)
                l.append(0)
                return l
            else:
                first_list.append(last_digit + 1)
                return first_list


s = Solution()

l = s.plusOne([0])

print(l)
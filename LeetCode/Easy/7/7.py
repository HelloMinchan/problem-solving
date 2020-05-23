class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0;
        elif x > 0:
            t = int(str(x)[::-1])
            if t > 2147483647:
                return 0
            else:
                return t
        else:
            t = int((str(x)[1:])[::-1])
            if t > 2147483647:
                return 0
            else:
                return t * -1

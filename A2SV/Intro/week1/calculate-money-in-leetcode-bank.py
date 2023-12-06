class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        total_money = 0
        monday=1
        number_weeks = n // 7

        number_days = n%7

        for i in range(number_weeks):

            total_money += (7*( 2*monday  + 6 ) )/2
            monday += 1

        total_money += ((number_days*(2* monday + number_days - 1))/2)

        return total_money

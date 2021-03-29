class Solution:
    def numberToWrods(self, num: int) -> str:
        # base case
        if num == 0:
            return "Zero"

        def convertThreeDigit(num):

            convert1 = {
                0: "Zero",
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen",
            }

            convert3 = {
                0: "",
                1: "Ten",
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety",
            }

            if num == 0:
                return ''

            s = ''

            if num > 99:
                s = s + convert1[num // 100] + "Hundred"

            if num > 19:
                s = s + convert3[num // 10] + ''
                num = num % 10

            if num > 0:
                s = s + convert1[num]

            return s.strip()

        final = ''
        count = 0
        levels = ['', ' Thousand', ' Million', ' Billion', ' Trillion']

        while num > 0:
            three = num % 1000
            num = num // 1000
            words = convertThreeDigit(three)
            if words:
                final = words + levels[count] + final
            count += 1
        return final.strip()


S = Solution()
num = 12345
print(S.numberToWrods(num))

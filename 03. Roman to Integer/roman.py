#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s):
        roman = {}
        roman['I'] = 1
        roman['V'] = 5
        roman['X'] = 10
        roman['L'] = 50
        roman['C'] = 100
        roman['D'] = 500
        roman['M'] = 1000
        s = list(s)
        count = 0
        for ind,num in enumerate(s):
            print(f'num is {num}')
            if ind > 0:
                if roman[s[ind-1]] < roman[num]:
                    continue
            if ind < len(s)-1:
                print(f'not the final item in list')
                print(f'roman numeral value for the next item is {roman[s[ind+1]]}')
                if roman[s[ind+1]] > roman[num]:
                    print(f'roman numeral value for next item is greater than current item {roman[num]}')
                    count += (roman[s[ind+1]]-roman[num])
                else:
                    count += roman[num]
            elif ind == len(s)-1:
                if roman[s[ind-1]] < roman[num]:
                    continue
                else:
                    count += roman[num]
        return count

new = Solution()
print(new.romanToInt('LVIII'))
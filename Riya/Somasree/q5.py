roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, S: str) -> int:
        ans = 0
        for i in range(len(S) - 1, -1, -1):
            print("checking value", S[i],i)
            num = roman[S[i]]
            print("num", num)

            if 4 * num < ans:
                ans -= num
                print("calculaten biyog", ans)
            else:
                ans += num
                print("calculaten sum", ans)
        return ans



c=Solution()
print(c.romanToInt('MCMXCIV'))

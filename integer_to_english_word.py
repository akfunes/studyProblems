# https://leetcode.com/problems/integer-to-english-words/
class Solution:
    def onesToWords(self,num):
        if num == 1:
            return "One"
        elif num == 2:
            return "Two"
        elif num == 3:
            return "Three"
        elif num == 4:
            return "Four"
        elif num == 5:
            return "Five"
        elif num == 6:
            return "Six"
        elif num == 7:
            return "Seven"
        elif num == 8:
            return "Eight"
        elif num == 9:
            return "Nine"

    def tensToWords(self, num):
        if num < 10:
            return self.onesToWords(num)
        elif num >= 10 and num < 20:
            if num == 10:
                return "Ten"
            elif num == 11:
                return "Eleven"
            elif num == 12:
                return "Twelve"
            elif num == 13:
                return "Thirteen"
            elif num == 14:
                return "Fourteen"
            elif num == 15:
                return "Fifteen"
            elif num == 16:
                return "Sixteen"
            elif num == 17:
                return "Seventeen"
            elif num == 18:
                return "Eighteen"
            elif num == 19:
                return "Nineteen"
        elif num >= 20 and num < 30:
            ans = "Twenty"
            if num % 10 > 0:
                ans = ans + " " + self.onesToWords(num%10)
            return ans
        elif num >= 30 and num < 40:
            ans = "Thirty"
            if num % 10 > 0:
                ans = ans + " " + self.onesToWords(num%10)
            return ans
        elif num >= 40 and num < 50:
            ans = "Forty"
            if num % 10 > 0:
                ans = ans + " " + self.onesToWords(num%10)
            return ans
        elif num >= 50 and num < 60:
            ans = "Fifty"
            if num % 10 > 0:
                ans = ans + " " + self.onesToWords(num%10)
            return ans
        elif num >= 60 and num < 70:
            ans = "Sixty"
            if num % 10 > 0:
                ans = ans + " " + self.onesToWords(num%10)
            return ans
        elif num >= 70 and num < 80:
            ans = "Seventy"
            if num % 10 > 0:
                ans = ans + " " + self.onesToWords(num%10)
            return ans
        elif num >= 80 and num < 90:
            ans = "Eighty"
            if num % 10 > 0:
                ans = ans + " " + self.onesToWords(num%10)
            return ans
        elif num >= 90 and num < 100:
            ans = "Ninety"
            if num % 10 > 0:
                ans = ans + " " + self.onesToWords(num%10)
            return ans

    def hundredsToWord(self,num):
        ans = ""
        if num >= 100 and num < 1000:
            ans = self.onesToWords(num//100) + " Hundred"
            num = num % 100
            if num < 100 and num > 0:
                ans += " " + self.tensToWords(num)
        else:
            ans += self.tensToWords(num)
        return ans

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ans = ""
        i = 0
        div = 1000
        while num > 0:
            digits = num % div
            if digits > 0:
                word = self.hundredsToWord(digits)

                if i == 0:
                    ans = word
                if i == 1:
                    ans = word + " Thousand " + ans
                if i == 2:
                    ans = word + " Million " + ans
                if i == 3:
                    ans = word + " Billion " + ans

            i+=1
            num = num//div

        return str.strip(ans)

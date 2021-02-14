# https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars: List[str]) -> int:
        lenChars = len(chars)
        if lenChars == 1:
            return 1
            
        i = 0
        j = 1
        writePointer = 0
        
        while j <= lenChars:
            if j == lenChars or chars[i] != chars[j]:
                numConsecutive = j - i
                if numConsecutive == 1:
                    chars[writePointer] = chars[i]
                    writePointer += 1
                else:
                    # write the character first to the writePointer location
                    chars[writePointer] = chars[i]
                    writePointer += 1
                    # find and store the digits of the consecutive number count and write it to the list
                    digits = []
                    while numConsecutive > 0:
                        digits.append(str(numConsecutive%10))
                        numConsecutive = numConsecutive//10
                    for digitIndex in range(len(digits)-1,-1,-1):
                        chars[writePointer] = digits[digitIndex]
                        writePointer += 1
                i = j
            j += 1
            
            
        return writePointer

# https://leetcode.com/problems/utf-8-validation/
class Solution:
    def getNBytes(self, data):
        i = 0
        while i < len(data) and data[i] != "0":
            i += 1
            
        return i
    
    def validUtf8(self, data: List[int]) -> bool:
        nBytes = 0
        
        for item in data:
            currByte = format(item,'#010b')[-8:]
            
            if nBytes == 0:
                nBytes = self.getNBytes(currByte)
                
                if nBytes == 0:
                    continue
                elif nBytes == 1 or nBytes > 4:
                    return False
            else:
                if len(currByte) < 8 or currByte[0] != "1" or currByte[1] != "0":
                    return False
            nBytes -= 1
            
        return nBytes == 0

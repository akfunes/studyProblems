# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.buffer = []
        self.len = 0

    def updateBuffer(self, s):
        if(s):
            self.buffer = s
            self.len = len(s)
        else:
            self.buffer = []
            self.len = 0

    def move2buf(self, buf, n):
        numRead = min(n,self.len)
        for i in range(numRead):
            buf[i] = self.buffer[i]
            i+=1

        self.updateBuffer(self.buffer[numRead:])
        return numRead

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """

        if(self.len > n):
            return self.move2buf(buf,n)
        else:
            temp = [''] * 4
            read4(temp)
            if temp[0] != '':
                self.updateBuffer(self.buffer + temp)

            while self.len < n and temp[0] != '':
                temp = [''] * 4
                read4(temp)
                self.updateBuffer(self.buffer + temp)

            return self.move2buf(buf,n)


import heapq
def sol(nums):
    numDict = {}
    equalSums = {}
    for n in nums:
        digitSum = 0
        temp = n
        while temp > 0:
            digitSum += temp % 10
            temp = int(temp/10)
        if digitSum in numDict:
            if digitSum in equalSums:
                equalSums[digitSum].append(n)
            else:
                equalSums[digitSum] = [n , numDict[digitSum]]
        else:
            numDict[digitSum] = n

    ans = -1
    for v in equalSums.values():
        if(len(v) > 2):
            twoLargest = heapq.nlargest(2,v)
            s = sum(twoLargest)
        else:
            s = sum(v)
        if s > ans:
            ans = s
    return ans

def main():
    a = [51,71,17,42]
    #a = [42,33,60]
    print(sol(a))

main()

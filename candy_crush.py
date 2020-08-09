def sol2(s):
    if(len(s) <= 2):
        return s

    stack = []
    ans = ""
    for i in range(0, len(s)):
        print(stack)
        if len(stack) > 0:
            item = stack.pop()
            if item[0] == s[i]:
                item[1] +=1
                stack.append(item)
            else:
                # push the previous substring back to the stack if it is not long enough to pop
                if item[1] < 3:
                    stack.append(item)

                # push the current character to the stack after attempting to pop from the stack
                item = [s[i],1]
                if len(stack) > 0:
                    item2 = stack.pop()
                    if item2[0] == s[i]:
                        item = item2
                        item[1] +=1
                    else:
                        # push the previous substring back on to the stack if it does not match the current char
                        stack.append(item2)

                # push the current substring back onto the stack
                stack.append(item)
        # push character on to the stack if it is empty
        else:
            item = [s[i],1]
            stack.append(item)

    print(stack)
    # create the answer after making a last pass of removing substrings with enough characters
    for i in range(0,len(stack)):
        item = stack.pop()
        if(item[1] < 3):
            for j in range(0, item[1]):
                ans = item[0] + ans
    return ans

def sol(s):
    if(len(s) <= 2):
        return s

    x = 0
    y = 1
    while(x < len(s) and len(s) > 2 and y < len(s)):
        print(str(x) + " " + str(y) )
        if(s[x] == s[y]):
            y +=1

        else:
            if(y-x >= 3):
                s1 = s[0:x]
                s2 = s[y:]
                s = s[0:x] + s[y:]

                #print(s1)
                #print(s2)
                print(s)

                if(x > 0):
                    x = y -(y-x) -1
                    y = x+1
                    while (s[x] == s[y] and x > 0):
                        x -=1
                        print(x)
            else:
                x+=1
            y = x+1
    return s

def main():
    s = "aaabbbc"
    s = "aabbbacd"
    #s = "aabbccddeeedcba"
    print(s)
    print("ans " + sol2(s))

main()

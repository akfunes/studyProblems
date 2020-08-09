def sol(s):
    ans = 0
    ct = 0
    current = ""
    for c in s:
        if current == "":
            current = c
        elif current == c:
            ct += 1
        else:
            current = c
            if ct >= 3:
                ans = ans + int(ct/3)
                ct = 0
    if (ct >= 3):
        ans = ans + int(ct/3)
    return ans

def main():
    s = "baaaaa"
    s = "baaabbaabbba"
    s = "baabab"
    print(sol(s))

main()

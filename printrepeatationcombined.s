
#aaabccccaa
#a3b1c4a2

def printpair(s1):
    prev = ''
    repeat = 1
    for i in range(1,len(s1)):
        prev = s1[i-1]
        current = s1[i]
        if prev == current:
            repeat += 1
        else:
            print(prev,repeat)
            repeat = 1
    print(current,repeat)
printpair('aaabcccccaa')
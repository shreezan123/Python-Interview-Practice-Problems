def reversenum(num):
    ans = 0
    process = 0
    a=1
    fakenum = num
    while fakenum > 0:
        fakenum = fakenum // 10
        process += 1
    for i in range (0, process-1):
        a *= 10
    while num > 0:
        rem = num % 10
        ans += rem * a
        a = a//10
        num = num // 10
    return ans
print(reversenum(123))
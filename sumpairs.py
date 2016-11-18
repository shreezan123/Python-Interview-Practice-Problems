def sumnums(arr,sum):
    anslist = []
    dict = {}
    for each in arr:
        if each not in dict:
            dict[each] = 1
        else:
            dict[each] += 1
    print(dict)
    for each in dict:
        if dict[each] == 0:
            break
        target = sum - each
        if target in dict:
            anslist.append((each,target))
            dict[each] -= 1
            dict[target] -= 1
    return anslist
print(sumnums([1,2,3,2,4,0],4))
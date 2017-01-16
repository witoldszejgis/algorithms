def number_needed(a, b):
    aDict={}
    bDict={}
    for l in a:
        if l in aDict:
            aDict[l]+=1
        else:
            aDict[l]=1
    for l in b:
        if l in bDict:
            bDict[l]+=1
        else:
            bDict[l]=1
    changes=0
    alphabet=map(chr, range(97, 123))
    for l in alphabet:
        if l in aDict and l in bDict:
            changes+=abs(aDict[l]-bDict[l])
        elif l in aDict:
            changes+=aDict[l]
        elif l in bDict:
            changes+=bDict[l]
    return changes
            

a = input().strip()
b = input().strip()

print(number_needed(a, b))

def ransom_note(magazine, rasom):
    magDict={}
    for w in magazine:
        if w in magDict:
            magDict[w]+=1 
        else:
            magDict[w]=1
    ans=True
    for w in ransom:
        if w in magDict:
            if  magDict[w]==1:
                del magDict[w]
            else:
                magDict[w]-=1
        else:
            ans=False
    return ans

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')


ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

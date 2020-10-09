#if __name__ == '__main__':
#    s=[]
#    n=[]
#    for _ in range(int(input())):
#        name = input()
#        n.append(name)
#        score = float(input())
#        s.append(score)

#    k = sorted(s)
#    temp=1
#    secondLowestScore = 0
#    if k[0]==k[temp]:
#        temp=temp+1
#    else:
#        secondLowestScore = k[temp]        
#    index = []
#    for j in range(len(s)):
#        if s[j]==float(secondLowestScore):
#            index.append(n[j])
#    index.sort()
#    for l in index:
#        print(l)
#    if any one can correct my commented code then ill be thankfull..
n=[]
s=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                n+=[[name,score]]
                s+=[score]
        b=sorted(list(set(s)))[1] 

        for a,c in sorted(n):
             if c==b:
                    print(a)

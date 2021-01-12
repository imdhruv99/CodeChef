for t in range(int(input())):
    
    N, M = map(int, input().split())
    Alist = list(map(int, input().split()))
    Blist = list(map(int, input().split()))
    
    i = 0
    flag = True
    
    while sum(Alist) <= sum(Blist):
        
        Alist.sort()
        Blist.sort()
        
        if Alist[0] < Blist[-1]:
        
            Alist[0], Blist[-1] = Blist[-1], Alist[0]
            i += 1
        
        else:
        
            flag = False
            print(-1)
            break
    
    if flag == True:
        print(i)

"""
Sample Input

2
2 3
2 2
5 5 5
4 3
1 3 2 4
6 7 8
1
1 3
2
2 2 2
"""

"""
Sample Output

2
1
-1
"""
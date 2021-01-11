## 30/100 Partial Solution

t = int(input())

for _ in range(t):
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    
    for a in A:
        neg = 0
        for i in range(1, len(a)):
            if a[i] < 0:
                neg+=1
        #print(neg)
        print(neg*(len(a)-neg -1))

"""
Sample Input

1
2
2 -2 1
1 2
"""

"""
Sample Output

2
"""
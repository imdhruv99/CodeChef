t = int(input())

for _ in range(t):
    n,k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    sum = h[0]
    s1 = set()

    res = -1

    s1.add(h[0])
    for i in range(1, len(h)):
        s2 = set()
        sum+=h[i]
        for ele in s1:
            s2.add(h[i])

            if (ele >=k  and sum - ele) >=k or (ele + h[i] >= k and sum - ele - h[i] >= k):
                res = i
                break
            s2.add(ele + h[i])
            s2.add(ele)
        
        if res != -1:
            break
        
        s1 = s2

    if res == -1:
        print(res)
    else:
        print(res+1)

"""
Sample Input

2
8 38
7 8 19 7 8 7 10 20
4 5
2 10 4 9
"""

"""
Sample Output

7
2
"""
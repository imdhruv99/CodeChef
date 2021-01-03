for t in range(int(input())):
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    P = sum(A)//K
    print(min(P, D))
    
 """
Sample Input
 
5
1 5 31
4
1 10 3
23
2 5 7
20 36
2 5 10
19 2
3 3 300
1 1 1
 """
 
 """
 Sample Output
 
0
2
7
4
1
 """
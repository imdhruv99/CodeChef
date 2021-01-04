for t in range(int(input())):
    
    N, K, x, y = map(int, input().split())
    
    if x == y:
        print(N, N)
    
    else:
        data_list = []
        if x < y:
            value1 = [x + N - y, N]
            value2 = [N, N - y + x]
            value3 = [y - x, 0]
            value4 = [0, y - x]
            data_list = [value1, value2, value3, value4]
        else:
            value5 = [N, y + N - x]
            value6 = [y + N - x, N]
            value7 = [0, x - y]
            value8 = [x - y, 0]
            data_list = [value5, value6, value7, value8]
    
        t = data_list[(K - 1) % 4]
        print(t[0], t[1])


"""
Sample Input

2
5 5 4 4
5 2 3 1
"""

"""
Sample Output

5 5
3 5
"""
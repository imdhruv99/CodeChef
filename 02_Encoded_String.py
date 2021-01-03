data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

for t in range(int(input())):
    num = int(input())
    s = input()
    string = ''
    for i in range(0, num-3, 4):
        string+=data[int(s[i:i+4], 2)]
    print(string)
	
"""
Sample Input

3
4
0000
8
00001111
4
1001
"""

"""
Sample Output

a
ap
j
"""
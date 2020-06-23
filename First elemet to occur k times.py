'''Given an array of N integers. The task is to find the first element that occurs K number of times. If no element occurs K times the print -1.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains an integer N denoting the size of an array and the number K. The second line of each test case contains N space separated integers denoting elements of the array A[ ].

Output:
For each test case in a new line print the required answer.

Constraints:
1 <= T <= 100
1 <= N, K <= 105
1<= A <= 106

Example:
Input :
1
7 2
1 7 4 3 4 8 7
Output :
7 '''

#code
from collections import OrderedDict
for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    nCount,res = OrderedDict(), -1
    for elem in arr:
        if elem in nCount:
            nCount[elem] += 1
        else:
            nCount[elem] = 1
    for key in nCount.keys():
        if nCount[key] == m:
            res = key
            break
    print(res)

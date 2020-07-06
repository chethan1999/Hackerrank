Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

#code
from itertools import combinations
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    res = combinations(arr,3)
   
    # for every element in arr 
    # check if a pair exist(in array) whose 
    # sum is equal to arr element 
    i = n - 1
    c = 0
    for ele in res:
        if(ele[0]+ele[1]==ele[2]):
            c += 1
    # no such triplet is found in array 
    if(c==0):
        print(-1)
        
    else:
        print(c)

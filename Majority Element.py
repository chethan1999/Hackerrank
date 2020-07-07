'''
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

Input:  
The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

Output: 
For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.

Constraints:
1 <= T<= 100
1 <= N <= 107
0 <= Ai <= 106

Example:
Input:
2
5
3 1 3 3 2
3
1 2 3

Output:
3
-1  '''

#code
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    c = Counter(arr)
    flag = 0
    half = n//2
    for key,val in c.items():
        if(val>half):
            print(key)
            flag = 1
            break
    if(flag==0):
        print(-1)

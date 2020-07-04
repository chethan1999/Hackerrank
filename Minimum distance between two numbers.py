'''You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

Input :
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. The first line of each test case contains an integer N denoting size array. Then in the next line are N space separated values of the array A. The last line of each test case contains two integers  x and y.

Output :
Print the minimum index based distance between x and y.

Your Task:
Complete the function minDist() which takes the array, n, x and y as input parameters and returns the minimum distance between x and y in the array. If no such distance is possible then return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
1 <= N <= 105
0 <= A[i], x, y <= 105

Example:
Sample Input:
2
4
1 2 3 2
1 2
7
86 39 90 67 84 66 62 
42 12

Sample Output:
1
-1 '''


def minDist(arr, n, x, y):
    i=0
    p=-1
    min_dist = 10000; 
      
    for i in range(n):  
      
        if(arr[i] ==x or arr[i] == y):   
            if(p != -1 and arr[i] != arr[p]): 
                min_dist = min(min_dist,i-p) 
            
            p=i 
           
    if(min_dist == 10000): 
       return -1
    return min_dist 

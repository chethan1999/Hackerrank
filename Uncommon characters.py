'''Find and print the uncommon characters of the two given strings S1 and S2. Here uncommon character means that either the character is present in one string or it is present in other string but not in both. The strings contains only lowercase characters and can contain duplicates.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two strings in two subsequent lines.

Output:
For each testcase, in a new line, print the uncommon characters of the two given strings in sorted order.

Constraints:
1 <= T <= 100
1 <= |S1|, |S2| <= 105

Example:
Input:
1
characters
alphabets
Output:
bclpr '''

#code
for _ in range(int(input())):
    s1 = input()
    s2 = input()
    
    l = []
    for c1 in s1:
        for c2 in s2:
            if c1 not in s2:
                l.append(c1)
                
            if c2 not in s1:
                l.append(c2)
                
    l = sorted(set(l))
    res = ""
    for ele in l:
        res += ele
    print(res)

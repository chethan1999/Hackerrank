from collections import deque
d = deque()
s = input("Enter a string whose brackets to be matched: ")

top = -1
flag = 0
for ele in s:
    if top==-1 and (ele==')' or ele==']' or ele=='}'):
        print("Not Matched")
        flag = 1
        break
    
    if(ele=='(' or ele=='[' or ele=='{'):
        d.append(ele)
        top += 1

    elif(ele==')' and d[top]=='('):
        d.pop()
        top -= 1

    elif(ele==']' and d[top]=='['):
        d.pop()
        top -= 1

    elif(ele=='}' and d[top]=='{'):
        d.pop()
        top -= 1

    else:
        pass
if flag==0:
    if top==-1:
        print("Matched")

    else:
        print("Not Matched")

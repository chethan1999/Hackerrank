''' You are given a number of boxes containing variable number of balls. You will iteratively pick up the balls untill and unless there are no balls left in any box.
The condition is that during every iteration you have to select box that contain minimum number of balls, and pickup the same amount of balls from all other boxes.
If a box gets empty, you throw away that box. Given the initial number of balls in n boxes, print how many boxes are left before each iteration untill there are none left. '''

n = int(input())
arr = list(map(int,input().split()))
print(n,end=' ')

while(n>0):
    
    m = min(arr)
    for i in range(len(arr)):
        arr[i] -= m

    while(True):
        try:
            arr.remove(0)
            n -= 1
        except:
            break
    if n!=0:
        print(n,end=' ')

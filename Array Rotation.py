for _ in range(int(input())):
    nd = list(map(int,input().split()))
    n = nd[0]
    d = nd[1]
    arr = list(map(int,input().split()))
    
    for _ in range(d):
        i = 0
        first = arr[i]
        while(i<n-1):
            arr[i] = arr[i+1]
            i += 1
        arr[n-1] = first
        
    for ele in arr:
        print(ele,end=' ')
        
    print()

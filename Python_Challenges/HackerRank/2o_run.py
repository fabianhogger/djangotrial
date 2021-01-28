n = int(input())
arr =list(map(int, input().split()))
if(n>=2 and n<=10):
    if(all(arr)<=100 and all(arr)>=-100):
        arr=sorted(arr)
        mxx=max(arr)
        unique=[i for i in range(-100,mxx+1) if i in arr]
        print(unique[-2])

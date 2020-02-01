n = int(input())
arr = list(map(int, input().split()))
lar = max(arr)
i=0
while(i<n):
    if lar ==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))


arr = [2,3,5,64,3,8,9]

target = 64

arr.sort()

print(arr)

start = 0
end = len(arr) 
print(end)
mid = end//2

while (start <= end+1):
    print("the mid value is {}".format(arr[mid]))
    start+=1
    
    if arr[mid] == target:
        print("value is {}".format(target))
        break
    elif arr[mid] < target:
        mid +=1
        print("execute add")
    elif arr[mid] > target:
         mid -=1
         print("execute less")
    else:
        print("-1")

    
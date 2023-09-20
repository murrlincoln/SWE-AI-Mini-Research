def even_sort(arr): 

even = []

for i in arr:

if i % 2 == 0:

even.append(i)

even.sort()

for i in range(len(arr)):

if arr[i] % 2 == 0:

arr[i] = even.pop(0)

return arr
arr = [12,60,30,75,55,90,35,80,31]

temp = []
res = []
for i in range(len(arr) - 1, -1, -1):
    if not temp:
        temp.append(arr[i])
    elif arr[i] >= temp[0]:
        temp.append(arr[i])
    else:
        res.append(temp[::-1])
        temp = [arr[i]]
if temp:
    res.append(temp[::-1])
print(res[::-1])
     
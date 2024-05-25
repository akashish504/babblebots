arr = [12, 50, 15, 60, 9, 62, 10, 70, 15]

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
     
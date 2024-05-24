arr = [40,30,50,60,70,80,90,60,50,70]
res = []
i = 0
ascending =0
if arr[1] > arr[0]:
    ascending = 1
stack = []
to_break = False
while i < len(arr):
    if i == len(arr)-1:
        stack.append(arr[i])
        to_break = True
    else:
        if arr[i] > arr[i+1]:
            stack.append(arr[i])
            ascending = 0
        elif arr[i] < arr[i+1] and ascending == 0:
            stack.append(arr[i])
            ascending = 1
            to_break = True
        else:
            stack.append(arr[i])
    if to_break:
        top_el = stack.pop()
        temp_res = [top_el]
        while stack:
            el = stack.pop()
            if el >= top_el:
                temp_res.append(el)
            else:
                stack.append(el)
                break
        for j in range(len(stack)):
            res.append([stack[j]])
        res.append(temp_res[::-1])
        to_break = False
        stack = []
    i=i+1

print(res)


temp = []
new_res = []
for i in range(len(res) - 1, 0, -1):
    if res[i-1][-1] > res[i][-1]  :
        temp = res[i] + temp 
    else:
        temp = res[i] + temp
        new_res.append(temp)
        temp = []
if res[0][-1] > res[1][-1]  :
    temp = res[0] + temp
    new_res.append(temp)
else:
    if temp:
        new_res.append(temp)
    new_res.append(res[0])
print(new_res[::-1])
    

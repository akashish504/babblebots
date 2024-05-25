arr = [10,10,10,]
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

# At this point the solution in not optimal, it only considers local hills not the global hills.

# for eg
# for [12, 50, 15, 60, 10, 70, 15]

# the answer would be [[12], [50, 15], [60, 10], [70, 15]]

# So would need to rewrite the grouping logic. Which sort of culminates to optimal solution


temp = []
new_res = []
for i in range(len(res) - 1, 0, -1):
    if temp:
        if res[i-1][-1] >= temp[-1]  :
            temp = res[i] + temp 
        else:
            temp = res[i] + temp
            new_res.append(temp)
            temp = []
    else:
        if res[i-1][-1] >= res[i][-1]  :
            temp = res[i] 
        else:
            new_res.append(res[i])
if temp:
    if res[0][-1] >= temp[-1]:
        temp = res[0] + temp
        new_res.append(temp)
    else:
        new_res.append(temp)
        new_res.append(res[0])
else:
    new_res.append(res[0])

print(new_res[::-1])
    

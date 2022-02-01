
n = int(input())
list = []
for i in (input()).split():
    i = int(i)
    list.append(i)
count_list = []
count = 1

for i in range(0,n-1):
    if list[i]<=list[i+1]:
        count +=1
    else:
        count_list.append(count)
        count = 1
count_list.append(count)
print(max(count_list))
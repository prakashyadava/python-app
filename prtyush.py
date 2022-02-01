list_count = []
A = [6,6,6,6,6]
count = 0
for i in range(len(A)):
    temp = A[i]
    for j in range(len(A)):
        if (A[i] % A[j] == 0 or A[j] % A[i]==0):
            count = count+1
    list_count.append(count-1)
    count = 0
print(list_count)


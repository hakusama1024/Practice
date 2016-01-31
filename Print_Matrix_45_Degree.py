matrix = [[1],[2], [3], [4], [5], [6], [7], [8]]
n = len(matrix)
m = len(matrix[0])

res = []
for i in range(m+n-1):
    j = 0
    if i >= m:
        j = i-m+1
        i = m-1
        
    tmp = []
    while i >= 0 and j < n:
        tmp.append(matrix[j][i])
        i-=1
        j+=1
    res.append(tmp)

print(res)

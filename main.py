r = int(input())
c = int(input())
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        element = int(input())
        row.append(element)
    matrix.append(row)
l = []
for i in range(r):
    rowsum = 0
    for j in range(c):
        rowsum += matrix[i][j]
    l.append(rowsum)
print(l)

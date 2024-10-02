matrix = []
def get_matrix(n, m, value):
    for i in range(n):
            matrix.append([value]*m)

get_matrix(2,2,10)
result1 = matrix
print(result1)
matrix = []
get_matrix(3,5,42)
result2 = matrix
print(result2)
matrix = []
get_matrix(4,2,13)
result3 = matrix
print(result3)

# Первая матрица
print("Введите размерность матрицы A")
n,m = int(input()),int(input())
print(n,"x",m)
A = []
for i in range(0, n):
    A.append([])
for i in range(0, n):
    for j in range(0, m):
        print("Введите элемент матрицы А с индексом ", i + 1, j + 1, ":", end='')
        A[i].append(int(input()))
# Вторая матрица
print("Введите размерность матрицы B")
a,b = int(input()),int(input())
print(a,"x",b)
B = [ ]
for i in range(0, a):
    B.append([])
for i in range(0, a):
    for j in range(0, b):
        print("Введите элемент матрицы B с индексом ", i + 1, j + 1, ":", end='')
        B[i].append(int(input()))
# Вывод матрицы А
print('Матрица А:', end='')
for i in range(n):
    print()
    for j in range(m):
        print(A[i][j], end=' ')
print(sep='\n')
# Транспонированная матрица А
AA = []
for i in range(m):
    AA.append([])
    for j in range(n):
        AA[i].append([A[j][i]])
print('Транспонированная матрица А:', end='')
for i in range(m):
    print()
    for j in range(n):
        print(AA[i][j], end='')
print(sep='\n')
# Вывод матрицы В
print('Матрица B:', end='')
for i in range(a):
    print()
    for j in range(b):
        print(B[i][j], end='')
print(sep='\n')
# Транспонированная матрица B
BB = []
for i in range(b):
    BB.append([])
    for j in range(a):
        BB[i].append([B[j][i]])
print('Транспонированная матрица B:', end='')
for i in range(b):
    print()
    for j in range(a):
        print(BB[i][j], end='')
print(sep='\n')
# Перемножение матриц
if m == a:
    C = []
    for i in range(n):
        C.append([])
        for j in range(b):
            for a in range(n):
                C[i][j] += A[i][a] * B[a][j]
print("Результат умножения матрицы А на матрицу В:",C)
# Определитель
if b == 2 and n == 2:
    o = C[0][0]*C[1][1]-C[0][1]*C[1][0]
    print('Определитель матрицы С равен ', o)
elif b == 3 and n == 3:
    o = (C[0][0]*C[1][1]*C[2][2] + (C[0][1]*C[1][2]*C[2][0]) + (C[1][0]*C[2][1]*C[0][2])) - C[0][2]*C[1][1]*C[2][0] - C[0][1]*C[1][0]*C[2][2] - C[1][2]*C[2][1]*C[0][0]
    print('Определитель матрицы С равен ', o)

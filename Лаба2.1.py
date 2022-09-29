

b=int(input("Введите одно из предложенных действий: \n1)Транспонирование матрицы (возможные размеры матриц: 1х2, 2х1, 1х3, 3х1,2х2, 3х3) \n2)Умножение матриц (возможные размеры матриц: 1х2, 2х1, 1х3, 3х1, 2х2, 3х3)\n3)Определение ранга матрицы (возможные размеры матриц: 2х2, 3х3))\n"))
if b==1:
    print("Введите размерность матрицы")
    n, m = int(input("Строки:")), int(input("Столбцы:"))
    print(n, "x", m)
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            print("Введите элемент матрицы с индексом ", i + 1, j + 1, ":", end='')
            k = int(input())
            a[i].append(k)
    t=[]
    for i in range(n):
        print()
        for j in range(m):
            print(a[i][j],end=' ')
    print()
    for i in range(m):
        t.append([])
        for j in range(n):
            t[i].append(a[j][i])
    for i in range(m):
        print()
        for j in range(n):
            print(t[i][j],end=' ')

elif b==2:
    print("Введите размерность матрицы A")
    n, m = int(input("Строки:")), int(input("Столбцы:"))
    print(n, "x", m)
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            print("Введите элемент матрицы A с индексом ", i + 1, j + 1, ":", end='')
            k = int(input())
            a[i].append(k)
    for i in range(n):
        print()
        for j in range(m):
            print(a[i][j], end=' ')
    print()
    print("Введите размерность матрицы B:",m, "x",end=' ')
    g = int(input())
    b = []
    for i in range(m):
        b.append([])
        for j in range(g):
            print("Введите элемент матрицы B с индексом ", i + 1, j + 1, ":", end='')
            k = int(input())
            b[i].append(k)
    for i in range(m):
        print()
        for j in range(g):
            print(b[i][j], end=' ')
    print()
    c = []
    for i in range(n):
        c.append([])
        for j in range(g):
            c[i].append(0)
    for i in range(n):
        for j in range(g):
            for u in range(n):
                for p in range(m):
                    c[i][j] += a[u][p] * b[u][j]
    print("Результат умножения матрицы А на матрицу В:", c)

















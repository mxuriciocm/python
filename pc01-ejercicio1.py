def imprimeCombinaciones(n):
    def combinaciones(n, actual, inicio):
        if n == 0:
            print("{", ", ".join(map(str, actual)), "}")
            return
        for i in range(n, inicio - 1, -1):
            actual.append(i)
            combinaciones(n - i, actual, i)
            actual.pop()

    combinaciones(n, [], 1)

imprimeCombinaciones(5)




# Se introduce el numero de casos (t)
# Se introducen tantas palabras como casos (line)
# Para cada letra (c) de cada palabra (line)
# Si el indice (i) es par --> lo guardo en un sitio (first)
# Si es impar, en otro (second)



t = int(input ('number of test case: '))
for _ in range(t):
    line = input('Introduce el string: ')
    first = ""
    second = ""

    for i, c in enumerate(line):
        # print (i, c, i & 1)
        if (i & 1) == 0:
            first += c
        else:
            second += c
    print (first, second)
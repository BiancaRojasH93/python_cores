# 1 BÁSICO

for i in range(0, 101):
    print(i)

# 2 MÚLTIPLES DE 2

for i in range (2, 501):
    if i % 2 == 0:
        print(i)

# 3 CONTANDO VANILLA ICE

for i in range (1, 101):
    if i % 10 == 0:
        print ("Baby")
    elif i % 5 == 0:
        print("Ice Ice")
    else:
        print(i)

# 4 WOW NÚMERO GIGANTE A LA VISTA

sumaTotal = sum(i for i in range(0, 500000, 2))
print (sumaTotal)


# 5 REGRÉSAME AL 3

for i in range (2024, 0, -3):
    print (i)

# 6 CONTADOR DINÁMICO

numInicial = 3
numFinal = 10
multiplo = 2

for i in range (numInicial, numFinal+1):
    if i % multiplo == 0:
        print(i)
    else:
        i+1
# Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma tuturor numerelor introduse.
#  Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14.
nr=1
suma_nr=0
while nr!=0:
    nr=eval(input("numarul nenul:"))
    suma_nr+=nr
print(suma_nr)
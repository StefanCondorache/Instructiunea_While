# Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. 
# Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
# Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  Date de ieşire  medie_poz=12.55  medie_neg=-3.33   .
luna=1
nr_poz=0
nr_neg=0
total_poz=0
total_neg=0
while luna<13:
    temp=eval(input("temperatura:"))
    if temp>=0:
        temp_p=temp
        nr_poz+=1
        total_poz+=temp_p
    elif temp<0:
        temp_n=temp
        nr_neg+=1
        total_neg+=temp_n
    luna+=1
if nr_neg==0:
    medie_p=total_poz/nr_poz
    print(round(medie_p,2))
elif nr_poz==0:
    medie_n=total_neg/nr_neg
    print(round(medie_n,2))
else:
    medie_p=total_poz/nr_poz
    medie_n=total_neg/nr_neg
    print(round(medie_p,2))
    print(round(medie_n,2))

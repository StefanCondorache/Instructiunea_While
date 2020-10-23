# Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură.
n=int(input("n="))
i=1
suma=0
produsul=1
nr_nr=0
while i<=n:
    nr=eval(input("nr="))
    suma+=nr
    produsul*=nr
    nr_nr+=1
    i+=1
media_a=suma/nr_nr
print("suma=",suma)
print("produsul=",produsul)
print("media_a",media_a)
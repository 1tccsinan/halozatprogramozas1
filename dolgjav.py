lista = [2, 4, 1, 8, 3]

#A1 lista elemeinek összege

osszeg = 0
for szam in lista:
    osszeg += szam
print(f"lista elemeinek összege: {osszeg}")
print(f"lista elemeinek összege: {sum(lista)}")

#B1 lista elemeinek darabszáma
darab = 0
for _ in lista:
    darab +=1
print(f"lista elemeinek darabszáma: {darab}")
print(f"lista elemeinek darabszáma: {len(lista)}")

#A2 párosszámok átlaga
paros_osszeg = 0
paros_db = 0

for szam in lista:
    if szam %2 == 0:
        paros_osszeg += szam
        paros_db += 1
print(f"páros számok átlaga: {paros_osszeg / paros_db:.3}")


parosok_lista = [szam for szam in lista if szam % 2 == 0]
print(f"paros szamok atlaga : {sum(parosok_lista) / len(parosok_lista)}")



for i in lista:
    print(f"{i}: {i*"*"}")
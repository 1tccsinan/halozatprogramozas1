#ciklusok

lista = [1, 2, 3, 4, 5]


def osszegez(lista):
    osszeg = 0
    for elem in lista :
        osszeg += elem
    return osszeg



print(f"A lista elemeinek osszege: {osszegez(lista)}")


db = 0
for elem in lista:
    if elem % 2 == 0:
        db += 1

print("Páros számok darabszáma:", db)


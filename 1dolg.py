#B csoport.

# B.1. Számok darabszáma: 5
# B.2. Páros számok darabszáma: 3
# AB.3. Sávdiagram:
# 2: **
# 4: ****
# 1: *
# 8: ********
# 3: ***


lista = [2, 4, 1, 8, 3]

#1. feladat
print(f"Számok darabszáma: {len(lista)}") 

#2. feladat

db = 0
for elem in lista:
    if elem %2 == 0:
        db += 1 

print(f"Páros számok darabszáma: {db}")

3#.feladat

for i in lista:
    print(f"{i}: {i*"*"}")

# A róka libát lop a faluból, a hét minden napján egyet. Ezek súlyát tároltuk el a libak.txt-ben. A farkas várja a falu határában a rókát és a 3 kg-nál nehezebb libát elveszi, a kisebbeket meghagyja a rókánál.

# 0. Beolvasás
libak = []
with open("libak.txt") as fin:
    for suly in fin:
        libak.append(int(suly.strip()))
print(libak)
# 1. Hány kiló libát evett a róka a héten?
roka_kg = 0
for suly in libak:
    if suly <= 3:
        roka_kg += suly
print(f"A róka {roka_kg} kiló libát evett a héten")

# 2. Átlagosan hány kilósak a rókánál maradt libák?
roka_libak = []
for suly in libak:
    if suly <= 3:
        roka_libak.append(suly)

atlag = sum(roka_libak)/len(roka_libak)
print(f"Átlagosan {atlag} kilósok a rókánál maradt libák")

# 3. Előfordult-e, hogy a róka legalább 3kg-os libát lopott?
volt_e = None
for liba in libak:
    if liba >= 3:
        volt_e = True
        break

if volt_e:
    print(f"Előfordult, hogy a róka legalább 3kg-os libát lopott ")
else:
    print(f"Nem fordult elő, hogy a róka legalább 3kg-os libát lopott ")
   
        
# 4. Előfordult-e, hogy a róka kisebb libát lopott, mint az előző napon?


# 5. Hányadik napon sikerült először 3kg-nál nehezebb libát lopni?
# 6. Volt-e 6kg súlyú liba, ha volt akkor melyik napon?
# 7. Hány liba jutott a héten a farkasnak?
# 8. Hány kilós volt a rókánál maradó legnagyobb libának?



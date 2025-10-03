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
volt_kisebb = False
for index in range(len(libak)-1):
    if libak[index] > libak[index+1]:
        volt_kisebb = True
        break

if volt_kisebb:
    print(f"Előfordult, hogy a róka kisebb libát lopott, mint az előző napon")
else:
    print(f"Nem előfordult, hogy a róka kisebb libát lopott, mint az előző napon")

# 5. Hányadik napon sikerült először 3kg-nál nehezebb libát lopni?
i = 0
while not (libak[index] > 3):
    index += 1
print(f"{index+1} napon sikerült először 3kg-nál nehezebb libát lopni")
# 6. Volt-e 6kg súlyú liba, ha volt akkor melyik napon?
volt_6kg = None
for i in range(len(libak)):
    if libak[i] == 6:
        volt_6kg = i + 1
        break


# 7. Hány liba jutott a héten a farkasnak?
farkas_liba=[]
for liba in libak:
    if liba > 3:
        farkas_liba.append(liba)

print(farkas_liba)
print(f"{len(farkas_liba)}")
# 8. Hány kilós volt a rókánál maradó legnagyobb libának?

max_index = 0
for index in range(len(libak)):
    if libak[index] > libak[max_index]:
        max_index = index
print(f"{libak[max_index]} kilós volt a rókánál maradó legnagyobb libának")


with open ("libak_jo.txt", "w", encoding ="utf-8") as fout:
    for liba in libak:
        print(liba*1.1, file=fout)
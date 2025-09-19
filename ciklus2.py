#Kérjünk be számokat és adjuk meg az összegüket

# while bennmaradasi feltétel:
#     ciklus mag



# osszeg = 0
# be_szam=None
# while be_szam !=0 :
#     be_szam=int(input("Kérem a számot: "))
#     osszeg += be_szam

# print(f"A számok összege {osszeg}")

# print()


osszeg = 0

while True:
    be_szam = input("Kérem a számot (Enter a kilépéshez): ")
    if be_szam == "":   # ha üres enter
        break
    osszeg += int(be_szam)

print(f"A számok összege: {osszeg}")
print()
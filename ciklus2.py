#Kérjünk be számokat és adjuk meg az összegüket

# while bennmaradasi feltétel:
#     ciklus mag



osszeg = 0
be_szam=None
while be_szam !=0 :
    be_szam=int(input("Kérem a számot: "))
    osszeg += be_szam

print(f"A számok összege {osszeg}")


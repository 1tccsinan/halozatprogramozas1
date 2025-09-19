#kérjünk be 0 végjelig számokat és írjuk ki az összegüket

# osszeg=0
# while True:
#     be_szam=int(input("kérek egy számot: "))
#     if be_szam != 0:
#         osszeg+=be_szam
#     else:
#         break

# print(f"a bekért számok összege {osszeg}")



# Enter végjelig kérjen be számokat és írja ki az összegüket:

# osszeg=0
# while True:
#     be_szam = input("Kérem a számot (Enter a kilépéshez): ")
#     if be_szam == "":   
#         break
#     osszeg += int(be_szam)

# print(f"A számok összege: {osszeg}")


#kérjél be egy számot es 0 tól eddig a páros számokat irasd ki
hatar = int(input(f"Kérem a határ számot:"))
szam1 = 0
while szam1 != hatar+1:
    if szam1 % 2 ==0:
        print(szam1)
    szam1+=1
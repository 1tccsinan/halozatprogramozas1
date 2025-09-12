print ("Szia", end=" ")
print("Tibi")
print("Szia", "Tóth", "Karcsi", "!", sep="")
print("Szia Tóth Karcsi")
nev = "Tóth Karcsi"
print(f"Szia {nev}!")
print("Szia", "Peti", sep="\n", end="!") #\t
#adattipusok
# int()
# float()
# str()
# bool()
# list()
# set()
#tupple()
print()
print(int("5"))
print(float(5))
print(str(5.0))
print(bool(-1))
print(["hétfő", "kedd", "szerda"])
napok=["Hétfő", "kedd", "szerda"]
print(f"Napok: {napok}")
nevek = ["Tibi", "Sanyi", "Tibi"]
print(f"Nevek: {set(nevek)}")
print(tuple([1,2,3]))



#HF: git parancsok:
#git init : adott mappa verziókövetésének indítása
#git add. :

# Parancs	Leírás
# git init	Új Git repository inicializálása
# git clone <repo-url>	Repository letöltése GitHub-ról
# git status	Módosítások állapotának ellenőrzése
# git add <fájl>	Fájl hozzáadása a staging area-hoz
# git add .	Minden módosított fájl hozzáadása
# git commit -m "üzenet"	Módosítások commitolása
# git push	Módosítások feltöltése GitHub-ra

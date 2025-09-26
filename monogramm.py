#bekell kérni egy nevet és adja vissza a monogrammját pl: varga gyula vgy

#Csipes Nándor, Ladányi Levente

nev = input("Kérem a teljes nevet: ")
ket_vagy_haromjegyu_kezdetek = ["dzs", "gy", "cs", "sz", "zs", "ty", "ly", "ny", "dz"]

szavak = nev.strip().lower().split()
mg = ""

for szo in szavak:
    if not szo: 
        continue
    
    kezdet = "" 
    
    if len(szo) >= 3 and szo[:3] == "dzs":
        kezdet = szo[:3]
    elif len(szo) >= 2 and szo[:2] in ket_vagy_haromjegyu_kezdetek:
        kezdet = szo[:2]
    else:
        kezdet = szo[0]

    mg += kezdet[0].upper() + kezdet[1:] if len(kezdet) > 1 else kezdet.upper()

print(f"A monogram: {mg}")
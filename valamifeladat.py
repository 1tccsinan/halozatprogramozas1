#bekell kérni egy nevet és adja vissza a monogrammját pl: varga gyula vgy

nev = input("Kérem a teljes nevet: ")
ketjegyu_kezdetek = ["gy", "cs", "sz", "zs", "ty", "ly", "ny", "dz","dzs"]

szavak = nev.strip().lower().split()
mg = ""

for szo in szavak:
    if not szo: 
        continue
    if len(szo) >= 3 and szo[:3] in ketjegyu_kezdetek:
        mg += szo[:3]
    else:
        mg += szo[0]

print(f"A monogram: {mg}")

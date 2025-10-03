
nev = input("Kérem a teljes nevet: ")

# ket_vagy_haromjegyu_kezdetek = ["dzs", "gy", "cs", "sz", "zs", "ty", "ly", "ny", "dz"]

szavak = nev.strip().lower().split()

mg = ""

for szo in szavak:
    if not szo: 
        continue
    
    kezdet = ""

    if len(szo) >= 3 and szo[0] == 'd' and szo[1] == 'z' and szo[2] == 's' and len(szo) >= 3 and szo[0:3] == "dzs":
        kezdet = szo[0:3] # 'dzs'
    
    elif len(szo) >= 2:
        # 'gy'
        if szo[0] == 'g' and szo[1] == 'y':
            kezdet = szo[0:2]
        # 'cs'
        elif szo[0] == 'c' and szo[1] == 's':
            kezdet = szo[0:2]
        # 'sz'
        elif szo[0] == 's' and szo[1] == 'z':
            kezdet = szo[0:2]
        # 'zs'
        elif szo[0] == 'z' and szo[1] == 's':
            kezdet = szo[0:2]
        # 'ty'
        elif szo[0] == 't' and szo[1] == 'y':
            kezdet = szo[0:2]
        # 'ly'
        elif szo[0] == 'l' and szo[1] == 'y':
            kezdet = szo[0:2]
        # 'ny'
        elif szo[0] == 'n' and szo[1] == 'y':
            kezdet = szo[0:2]
        # 'dz'
        elif szo[0] == 'd' and szo[1] == 'z':
            kezdet = szo[0:2]
        else:
            kezdet = szo[0]
            
        kezdet = szo[0]

   
    if len(kezdet) > 1:
        mg += kezdet[0].upper() + kezdet[1:]
    else:
        mg += kezdet.upper()

print(f"A monogram: {mg}")


szamok = [1,1,2,2,4,5,2,1,3]
# egyes_db = 0
# kettes_db = 0
# harmas_db = 0
# negyes_db = 0
# otos_db = 0


# for szam in szamok:
#     if szam == 1:
#         egyes_db += 1
#     elif szam == 2:
#         kettes_db += 1
#     elif szam == 3:
#         harmas_db += 1
#     elif szam == 4:
#         negyes_db += 1
#     elif szam == 5:
#         otos_db += 1
    
# print(f"Az 1-es számból ennyi darab van: {egyes_db} ")
# print(f"Az 2-es számból ennyi darab van: {kettes_db} ")
# print(f"Az 3-es számból ennyi darab van: {harmas_db} ")
# print(f"Az 4-es számból ennyi darab van: {negyes_db} ")
# print(f"Az 5-es számból ennyi darab van: {otos_db} ")
         

# for i in range(1,6):
#     print(f"{i} ből van {szamok.count(i)}")

darab =  [0,0,0,0,0]

for szam in szamok:
    darab [szam-1] += 1

print(f"{darab}") 
for i in range(len(darab)):
    print(f"{i+1} bol van {darab[i]}")


gyumolcsok = ["eper", "dinnye"]
jegyek = [2,5]

gyumolcsok.append("alma")
jegyek.append(1)
print(jegyek)
print(gyumolcsok)
jegyek.sort()
print(jegyek)
gyumolcsok.remove("dinnye")
print(gyumolcsok)
gyumolcsok.insert(1,"banán")
print(gyumolcsok)
# gyumolcsok = []
jegyek.reverse()
print(jegyek)
print(gyumolcsok.index("banán"))
print(jegyek.count(5))

print(sum(jegyek))
print(min(jegyek))
print(max(jegyek))
print(len(jegyek))

#stringeket tartalmazó lista kiírasa
print(f"{', '.join(gyumolcsok)}")

#inteket tartalmazó lista kiírasa
print(f"{', '.join(map(str, jegyek))}")

#lista bejárása elemenként
for jegy in jegyek:
    print(jegy)

#lista bejárása index szerint
for i in range(len(gyumolcsok)):
    print(gyumolcsok[i])



mx = [ 
    [1,2,3],
    [4,5,6]
]

for sor in mx:
    # for oszlop in sor:
        #print (oszlop, end=",")
        print(",".join(map(str,sor)))

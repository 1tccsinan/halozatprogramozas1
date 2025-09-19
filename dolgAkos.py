nevek = ["Tibi", "Évi", "Sanyi", "Karcsi", "Lili"]
nemek = [1,2,1,1,2]

# 1. Hány fiu van?
# 2. Fiuk nevei:
# 3. Hany % a fiuk aranya

for i in range(len(nevek)):
    print (nevek [i])

fiunevek = []
for i in range(len(nevek)):
    if nemek[i] == 1:
        fiunevek.append(nevek[i])
print(fiunevek)
print(f"{len(fiunevek)} fiú név van")

print(f"{len(fiunevek) / len(nevek) *100} % a fiúk aránya")
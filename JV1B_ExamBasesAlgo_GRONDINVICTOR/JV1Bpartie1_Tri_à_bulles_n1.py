

myTable  = [36,24]

for j in range(len(myTable)):
    valMax = 100
    for i in range(j,len(myTable)):
        if(myTable[i]<valMax):
            valMax = myTable[i]
            indiceMax = i
    save = myTable[j]
    myTable[j] = myTable[indiceMax]
    myTable[indiceMax] = save

print(myTable)
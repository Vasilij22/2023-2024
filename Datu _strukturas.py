#Objekts klasei dictionary
#vardnica = {"1":"viens","1":"viens"} 

#print(vardnica.keys())

#Rindas qeque

from collections import deque

rinda = deque()

rinda.append(["Vārna","Stārķis","Erglis"])
print("Rinda:", rinda) 

rinda.append("Kaija") #Pievienojam elementu rindas labaja puse
print("Pievienota Kaija:", rinda)

rinda.appendleft("Zilite") #Pivienojam elementu rindas kreisaja puse 
print("Pievienota Zilite:", rinda)

rinda.pop() #Noņemat elementu no labas puses
print("Noņemts elemnts:", rinda)

rinda.popleft() #Noņemat elementu no kreisas puses
print("Noņemts elements no kreisas puses:", rinda)

#Tuples - kortežs

#Sakarto nemainamo bet dublejamo viena veida neindeksetu elemntu kopa
#Nemainams saraksts 

kortezs = ('Janvaris','Februaris','Marts')
print(type(kortezs))

print()

#Set - kopa

#Unikalu, nesakartotu elementu kolekciju

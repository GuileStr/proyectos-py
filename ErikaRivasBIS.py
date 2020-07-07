preguntas = [
        {"What's the biggest planet in the universe":{"Omegacheron":"true","Taiti":"false"}},
        {"Where's the nearest Domino's pizza":{"20 nov":"true","Parque":"false"}},
        {"preg3":"xd"},
        {"preg4":"jeje"}]
np=[]
cuales=[0,1]
qu=[]
for i in cuales:
    np.append(preguntas[cuales[i]])
    #print(preguntas[cuales[i]])
for i in np:
    for u in i.keys():
        qu.append(u)
    #print(i.values())

# =============================================================================
# for i in np:
#     print("La pregunta completa es "+str(i))
#     for u in i.values():
#         print("Respuestas: "+str(u))
#         for a in u.keys():
#             print("Respuesta: "+str(a))
# =============================================================================
#print(np[0].get("What's the biggest planet in the universe"))


a=0
while a<10:
    for i in qu:
        print(i+"?")
        
        p1=int(input("Answer player 1: "))
        p2=int(input("Answer player 2: "))
    break

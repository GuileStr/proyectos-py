def find_all_hobbyists(hobby, hobbies):
    whoDo=[]#Una pequeña lista para guardar nombres
    for hob in hobbies: #Atrapar las llaves del diccionario
        for hobbi in hobbies[hob]: #Entrar a la lista dentro de cada llabe
            #print(hobbi)
            if hobbi==hobby: #Si el valor es igual al hobby a buscar
                whoDo.append(hob)
    return whoDo 
    
hobbies = { 
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}

print(find_all_hobbyists('Yoga', hobbies));

#Este lo saque al 100
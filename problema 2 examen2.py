def find_unique_numbers(numbers):
    cont= {i:numbers.count(i) for i in numbers} #diccionario donde i se convierte en la llave y hacemos un count
                                                #con ese mismo valor i, para buscar cuantas veces se repite
                                                #Damos vuelta a todo el list, y aunque se repita el numero
                                                #se sobreescribe y siempre dará el mismo valor con el count(i)
    selectedOnes=[] #Lista para seleccionar los que solo se repiten una vez
    for i in cont: #Ahora, ciclamos nuestro diccionario nuevo
        #print(i)       #Una mini pruba para ver si i si es la llave
        #print(cont[i]) #Una mini pruba para ver los values de cada llave
        if 0<cont[i]<2:   #Si el valor se repite menos de 2 veces y más de 0 (Obviamente esto solo es 1)
            selectedOnes.append(i) #Empujamos en los SelectedOnes la llave i
    return selectedOnes #Retornamos la lista de seleccionados

print(find_unique_numbers([1, 2, 1, 3, 5, 4, 5, 6]))

#A este me faltó eficientarlo
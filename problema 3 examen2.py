def tuple_slice(startIndex, endIndex, tup):
    #return tup[startIndex:endIndex] #Esto lo responde bien.. pero no regresa bien testCases ni nada
# =============================================================================
#     sliced=""   #
#     apoyo=0
#     apoyo2=len(tup)
#     #return tup[startIndex:endIndex]
#     for i in range(len(tup)):
#         #print(tup[i])
#         if i!=startIndex-1 and i!=endIndex:
#             sliced+=str(tup[i])
#         if apoyo<i<apoyo2-2:
#             sliced+=","
#     return sliced
# =============================================================================
    return str(tup[startIndex:endIndex])  #Creo que este es el perron

print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))

#Este se acabó el tiempo y solo resolvió un testCase
def generarSubredes(numSubRedes):
    subRedes = {}
    
    lista1 = []
    for i in range(1, numSubRedes + 1):
        lista1.append(f'Subred{str(i)}')
        
    lista2 = []
    for i in range(numSubRedes):
        lista2.append(None)
        
    subRedes.update({'Subred':lista1})
    subRedes.update({'Cantidad de hosts':lista2})
    
    return subRedes
    
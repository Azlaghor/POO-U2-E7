from classes import viajero

if __name__ == '__main__':
    viajeros = []
    with open('viajeros.txt', 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            instancia = viajero(datos[0],datos[1],datos[2],datos[3],int(datos[4]))
            viajeros.append(instancia)
    for viajerofrecuente in viajeros:
        viajerofrecuente.mostrarviajero()
    max_millas = 0
    viajeros_max_millas = []
        
    for viajero in viajeros:
        if viajero > max_millas:
            max_millas = viajero.get_millas()
            viajeros_max_millas = [viajero]
        elif viajero == max_millas:
            viajeros_max_millas.append(viajero)
    print(f'viajeros con mayor cantidad de millas {viajeros_max_millas}')
    codigo = input ('numero viajero frecuente:')
    encontrado = viajero ('','','','','')
    encontrado = viajeros.busqueda(codigo)
    if encontrado:
        num = input ('ingrese millas a acumular: \n')
        encontrado += num
        num = input ('ingrese millas a canjear: \n')
        encontrado -= num
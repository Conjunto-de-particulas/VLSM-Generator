import ipaddress
import math

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

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    else:
        raise ValueError("La dirección IP no es de clase A, B, o C")

def calculate_vlsm(network_address, num_subnets, listaNumHosts):
    # Convertir la dirección de red a un objeto IPv4Network
    network = ipaddress.IPv4Network(network_address, strict=False)
    
    # Obtener la clase de la dirección IP
    ip_class = get_ip_class(str(network.network_address))
    
    # Definir los límites de hosts por clase
    max_hosts_per_class = {
        'A': 16777214,  # 2^24 - 2
        'B': 65534,     # 2^16 - 2
        'C': 254        # 2^8 - 2
    }
    
    # Solicitar al usuario el número de hosts requeridos para cada subred
    print("Ingrese la cantidad de hosts requeridos para cada subred:")
    subnet_requirements = []
    for i in range(num_subnets):
        while True:
            try:
                hosts = listaNumHosts[i]
                if hosts < 0:
                    raise ValueError
                subnet_requirements.append(hosts)
                break
            except ValueError:
                print("Por favor, ingrese un número entero no negativo.")
    print(subnet_requirements)
                
    # Ordenar las subredes por el número de hosts requeridos (de mayor a menor)
    subnet_requirements.sort(reverse=True)
    
    # Lista para almacenar las subredes calculadas
    subnets = []
    
    # Dirección de inicio para la primera subred
    current_network = network.network_address
    total_hosts_allocated = 0
    
    for hosts in subnet_requirements:
        # Calcular el prefijo necesario para la cantidad de hosts
        required_prefix = 32 - math.ceil(math.log2(hosts + 2))  # +2 para red y broadcast
        
        # Calcular la subred temporal
        temp_subnet = ipaddress.IPv4Network((current_network, required_prefix), strict=False)
        
        # Verificar si la subred actual cabe dentro del rango de la red de clase C
        if total_hosts_allocated + (temp_subnet.num_addresses - 2) > max_hosts_per_class[ip_class]:
            break
        
        # Crear la subred real
        subnet = temp_subnet
        
        # Añadir la subred a la lista
        subnets.append(subnet)
        
        # Actualizar la cantidad de hosts asignados
        total_hosts_allocated += subnet.num_addresses - 2
        
        # Calcular la siguiente dirección de red disponible
        current_network = subnet.broadcast_address + 1
    
    # Mostrar mensaje si se alcanzaron los límites de la clase de red
    if total_hosts_allocated + (temp_subnet.num_addresses - 2) > max_hosts_per_class[ip_class]:
        print(f"Hasta aquí se puede realizar el proceso con esta IP ({network_address}). No se pueden asignar más subredes debido a las limitaciones de la clase de la red.")
    
    return subnets

def generarListaCantidadHosts(subRedes):
    
    list = []
    for i in range(len(subRedes['Cantidad de hosts'])):
        try:
            list.append(int(subRedes['Cantidad de hosts'][i]))
        except Exception as e:
            list.append(subRedes['Cantidad de hosts'][i])
    
    return list

def checkAllnoNone(lista):

    for i in lista:
        if type(i) != type(1):
            return False
    return True
        
    
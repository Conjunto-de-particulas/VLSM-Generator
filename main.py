import streamlit as st
import pandas as pd
import metodos

st.title('Subnetting VLSM')

dip = st.text_input('Direccion IP', '')
mr = st.text_input('Mascara de red(Abreviada)', '')
numSubRedes = st.text_input('Numero de subredes', '')

try:
    numSubRedes = int(numSubRedes)
except Exception as e:
    numSubRedes = 0

subRedes = metodos.generarSubredes(numSubRedes)
dfSubRedes = pd.DataFrame(subRedes)

edited_df = st.data_editor(dfSubRedes)
dfSubRedes = edited_df.copy()

direccionRed = f'{dip}/{mr}'
listaNumHosts = metodos.generarListaCantidadHosts(dfSubRedes)
results = {}
if metodos.checkAllnoNone(listaNumHosts) == True and len(listaNumHosts) > 0:
    
    print(direccionRed, listaNumHosts, len(listaNumHosts))
    subnets = metodos.calculate_vlsm(direccionRed, len(listaNumHosts), listaNumHosts)
    
    listOfList = []
    for i in range(7):
        listOfList.append([])

    for subnet in subnets:
        print(f"Subred: {subnet.network_address}/{subnet.prefixlen}, "
            f"Máscara de Subred: {subnet.netmask}, "
            f"Primera IP: {subnet.network_address + 1}, "
            f"Última IP: {subnet.broadcast_address - 1}, "
            f"Rango: {subnet.network_address + 1} - {subnet.broadcast_address - 1}, "
            f"Dirección de broadcast: {subnet.broadcast_address}, "
            f"Total de Hosts: {subnet.num_addresses - 2}")
        
        listOfList[0].append(f'{subnet.network_address}/{subnet.prefixlen}')
        listOfList[1].append(f'{subnet.netmask}')
        listOfList[2].append(f'{subnet.network_address + 1}')
        listOfList[3].append(f'{subnet.broadcast_address - 1}')
        listOfList[4].append(f'{subnet.network_address + 1} - {subnet.broadcast_address - 1}')
        listOfList[5].append(f'{subnet.broadcast_address}')
        listOfList[6].append(f'{subnet.num_addresses - 2}')
    results.update({'Subred': listOfList[0]})
    results.update({'Máscara de Subred': listOfList[1]})
    results.update({'Primera IP': listOfList[2]})
    results.update({'Última IP': listOfList[3]})
    results.update({'Rango': listOfList[4]})
    results.update({'Dirección de broadcast': listOfList[5]})
    results.update({'Total de Hosts': listOfList[6]})
    

dfResults = pd.DataFrame(results)
tablaResults = st.data_editor(dfResults)
        





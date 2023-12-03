def verifica_se_cabecote_esta_vazio(cabecote):
    estaVazio = True
    for elemento in cabecote:
        if elemento != '':
            estaVazio = False
            return estaVazio
    return estaVazio
    
def seleciona_indice_menor_elemento(cabecote):
    menor_elemento_indice = 0
    while cabecote[menor_elemento_indice] == '':
        menor_elemento_indice+=1
    for i in range(1, len(cabecote), 1):
        if(cabecote[i]==''):
            continue
        if(float(cabecote[i]) < float(cabecote[menor_elemento_indice])):
            menor_elemento_indice = i
    return menor_elemento_indice
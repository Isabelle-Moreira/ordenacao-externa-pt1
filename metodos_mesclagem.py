def verifica_se_cabecote_esta_vazio(cabecote):
    estaVazio = True
    for elemento in cabecote:
        if elemento != '':
            estaVazio = False
            return estaVazio
    return estaVazio

def verifica_se_tem_arquivo_vazio(cabecote):
    index_arquivo_vazio = None
    for index in range(len(cabecote)):
        if(cabecote[index]==''):
            index_arquivo_vazio = index
            return index_arquivo_vazio
    return index_arquivo_vazio

def verifica_se_cabecote_terminou_bloco(cabecote):
    terminouLeitura = True
    for elemento in cabecote:
        if elemento != '#\n':
            terminouLeitura = False
            return terminouLeitura
    return terminouLeitura
    
def seleciona_indice_menor_elemento(cabecote):
    menor_elemento_indice = 0
    while cabecote[menor_elemento_indice] == '' or cabecote[menor_elemento_indice] == '\n' or cabecote[menor_elemento_indice] == '#\n':
        menor_elemento_indice+=1
    for i in range(1, len(cabecote), 1):
        if(cabecote[i]=='' or cabecote[i]=='#\n'):
            continue
        if(float(cabecote[i]) < float(cabecote[menor_elemento_indice])):
            menor_elemento_indice = i
    return menor_elemento_indice


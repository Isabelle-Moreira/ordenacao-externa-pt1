import os
from ordenador import Ordenator

ordenador = Ordenator()

caminho_da_pasta ="./arquivos/"

if not os.path.exists(caminho_da_pasta):
    os.makedirs(caminho_da_pasta)
    
arquivo = open("teste1.txt", encoding='latin-1')
contador =0
nome_arquivo = ""
numero_arquivo=0
vetor_de_cem =[]
registros_por_arquivo=5
for linha in arquivo:
    #if(contador==0):
        #numero_arquivo+=1
        #nome_arquivo="arquivo"+str(numero_arquivo)+".txt"
        #novo_arquivo = open(nome_arquivo,"a")
    if(contador<registros_por_arquivo):
        vetor_de_cem.append(float(linha)) #vai atribuir os valores da linha do arquivo original no vetor
        contador+=1
        if(contador==registros_por_arquivo):
            #print(vetor_de_cem)
            numero_arquivo+=1
            nome_arquivo="arquivo"+str(numero_arquivo)+".txt" #nomeando novo arquivo
            caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo) #caminho completo arquivo + direcionamento para pasta
            #print(caminho_completo)
            novo_arquivo = open(caminho_completo,"a")  #criando novo arquivo já na pasta 

            ordenador.heap_sort(vetor_de_cem)

            for i in range(registros_por_arquivo):
                novo_arquivo.write(str(vetor_de_cem[i])+"\n")

            novo_arquivo.close()
            contador=0

            vetor_de_cem =[]

if(len(vetor_de_cem)>0):
    numero_arquivo+=1
    nome_arquivo="arquivo"+str(numero_arquivo)+".txt"
    caminho_completo = os.path.join(caminho_da_pasta,nome_arquivo)
    novo_arquivo = open(caminho_completo,"a")

    ordenador.heap_sort(vetor_de_cem)

    for i in range(len(vetor_de_cem)):
        novo_arquivo.write(str(vetor_de_cem[i])+"\n")

    novo_arquivo.close()

lista_arquivos = os.listdir(caminho_da_pasta)
print(lista_arquivos)
index_inicial =0
index_final = 5
incrementa_pros_proximos = 6



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


while index_inicial < len(lista_arquivos):
    contador_mesclagem = 0
    cabecote = [''] * 6
    lista_arquivos_abertos = [None] * 6

    for i in range(index_inicial, index_final+1, 1):
        caminho_completo = os.path.join(caminho_da_pasta, lista_arquivos[i])
        arquivo = open(caminho_completo)

        lista_arquivos_abertos[i%incrementa_pros_proximos] = arquivo

        cabecote[i%incrementa_pros_proximos] = lista_arquivos_abertos[i%incrementa_pros_proximos].readline()
    
    novo_arquivo_mesclado = open('mesclagem'+str(contador_mesclagem)+'.txt', "a")
    contador_mesclagem+=1

    #enquanto houver elementos no cabeçote:
    while not verifica_se_cabecote_esta_vazio(cabecote):
        print(cabecote)
        index_menor_elemento = seleciona_indice_menor_elemento(cabecote)

        #escreva o menor elemento no novo arquivo
        novo_arquivo_mesclado.write(cabecote[index_menor_elemento])
        arquivo = lista_arquivos_abertos[index_menor_elemento]
        cabecote[index_menor_elemento] = arquivo.readline()

    index_inicial += incrementa_pros_proximos
    index_final += incrementa_pros_proximos
        #mova o cabeçote do arquivo correspondente
